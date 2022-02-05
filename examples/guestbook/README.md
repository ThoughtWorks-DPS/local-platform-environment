## Example: Guestbook

The goal of this example is to demonstrate how helm can be configured to use a local registry and local deployment configuration to enable a single chart to support both local and remote development based on the environment configuration used. It is assumed you have minikube running locally with istio installed per as described in this repo.    

This example adapts the Kubernetes [guestbook-go](https://github.com/kubernetes/examples/tree/master/guestbook-go) example app.   

### Guestbook site

Suppose the twdps.io site is a Guestbook page where visitors can post comments.  

#### Namespaces convention (environments)

Each development team has a shorthand name used to identify their resources. A name might identify the business capability the team owns (such as the 'payments' team), or a name may just be a unique identifier chosen by the team members.  

The BlueManCrew (or just 'blue' for short) owns the guestbook app. 

The release pipeline environments represent the teams dedicated kubernetes namespaces in non-prod and production clusters. If the 'blue' team has three environments in their release pipeline such as Dev, QA, and Prod, then the respective namespaces could be:

blue-dev  
blue-qa  
blue-prod  

The namespace for the local minikube instance would then be:

blue-local  

To create the local namespace `blue-local` with istio-sidecar injection enabled, apply the following resource:
```
apiVersion: v1
kind: Namespace
metadata:
  name: blue-local
  labels:
    istio-injection: enabled
```

##### Local namespace helper

Use the invoke helper command `domain.add` to easily define an istio-enabled namespace based on team name plus "-local"  

```bash
$ inv ns.add blue
```

If you create a namespace some other way, be sure to annotate with:  

```yaml
labels:
  istio-injection: enabled
```

#### Domain and ingress

The guestbook app is hosted on the top-level domain `twdps.io` and the local environment will be `local.twdps.io`

Add the domain to your local hosts file:  
```bash
$ kubectl get svc istio-ingressgateway -n istio-system   # get the IP for the istio-ingressgateway
$ hostess add local.twdps.io EXTERNAL-IP                 # create a local entry, requires admin password
```

Create a certificate for the local domain using mkcert:
```
$ mkcert -cert-file local.twdps.io.crt -key-file local.twdps.io.key local.twdps.io "*.local.twdps.io"
$ kubectl create -n istio-system secret tls local.twdps.io-credential --key=local.twdps.io.key --cert=local.twdps.io.crt
```

To create an istio gateway that supports this local domain, deploy the following gateway resource:
```
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: local-gateway
  namespace: istio-system
  labels:
    app: local-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 443
      name: https-local
      protocol: HTTPS
    tls:
      mode: SIMPLE
      credentialName: local.twdps.io-credential
    hosts:
    - "local.twdps.io"
```

##### Local Ingress Helper

Use the invoke helper command `domain.add` to easily create local certs and deploy the local gateway.  

```bash
$ inv domain.add twdps.io
```

This will perform the following tasks:

1. create certificates for local.<parameter> with the local Root CA and deploy the local.<parameter>-credential to istio-system
1. deploy a local-gateway to manage ingress for local traffic on local.<parameter>  

#### Local Registry

When building locally and deploying to minikube, having a local container registry elimates the need to spam your actual registry with continuous iterative builds, while still supporting kubernetes deployments.  

Start minikube with  `--addons registry` and then run  
```
$ docker run -d --rm -it --name=registry-proxy --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"
```

You may now use `localhost:5000/myimage:tag` to push and pull incremental builds from this local registry.  

### Guestbook ui development example  

Starting from the examples/guestbook folder:  

The guestbook app is a simple bulletin board style message area where users can enter their name or other line of text and it will be echoed to the ui in a running list of all posts made. Posts are cached to an HA instance of redis.  

Both the cache and the guestbook app are deployed to kubernetes using Helm. The Charts for each app assume default values based on the local development context and are overridden at deploy time for remote environments.  

*First.* Deploy redis  

```
$ helm install redis charts/redis --namespace=blue-local --set version=v1.0.0
```

Note the following DestinationRule for the redis service:  
```
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: redis-master
  namespace: blue-local
spec:
  host: redis-master.blue-local.svc.cluster.local
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
        connectTimeout: 30ms
        tcpKeepalive:
          time: 7200s
          interval: 75s
    tls:
      mode: ISTIO_MUTUAL
  subsets:
  - name: default
    labels:
      app: redis
      version: v1.0.0
      role: master
```

This traffic policy causes Envoy to manage the number of connections to redis-master and a keepalive frequency.  

*Second.* Once the cache is running and ready to accept posts, we can begin active development on guestbook app  

• build the docker image  

We have a local registry available on localhost:5000, and by convention will use v0.0.0 to indicate local interations  
```bash
$ docker build -t localhost:5000/guestbook:local .
$ docker push localhost:5000/guestbook:local 
```

Now deploy the current local version of guestbook:
```
$ helm install guestbook charts/guestbook --namespace=blue-local --set version=local
```

You should be able to access the guestbook by directing your browser to `https://local.twdps.io`  

<p align="center"><img width="800" alt="guestbook" src="guestbook.png"></p>

Submit a couple messages to interact with the app.  

Now, let's make a change. Open public/index.html and change the text of the Submit button to `Post`  

Each time you build the docker image you will need to new tag, for this example we will assume:  

tag = local.<last commit SHA:1:8>.<next helm revision number>  

You can use `make local` to easily repeat these build steps.  

Build and deploy the changes:
```
$ make local
```

If you continuously refresh the guestbook page, you will see the text of the submit button begin to appear as 'Post' as the rolling upgrade proceeds. There are 3 replicas of the app running and as each is launch and returns a health status, traffic is moved and the old verions deleted. Within a few moments it will always have the new text.  


### Clean up

Use helm to uninstall the components of the guestbook app.  
```bash
$ helm uninstall guestbook --namespace=blue-local
$ helm uninstall redis --namespace=blue-local
```

[Return](doc/examples.md)
