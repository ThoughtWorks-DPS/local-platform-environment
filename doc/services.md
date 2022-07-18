### 4. Deploy supporting services to kubernetes  

The python `invoke` files in this repository provide a convenient way to install the following services.  

• [metrics-server](https://github.com/kubernetes-incubator/metrics-server)  
• [istio](https://istio.io)  
• open policy agent (pending)

_Use `invoke -l` to see a list of available shortcuts._  

### metric-server (hpa support) 

• metrics-server

If you started minikube using the invoke helper command then metrics-server is already running.  

Enter `$ minikube addons metrics-server enable` to start the api on an instance of minikube already running.  

You can confirm metrics-server is functioning correctly by hitting the endpoint:  

```
$ kubectl get --raw "/apis/metrics.k8s.io/v1beta1/nodes"
{"kind":"NodeMetricsList","apiVersion":"metrics.k8s.io/v1beta1","metadata":{},"items":[{"metadata":{"name":"minikube","creationTimestamp":"","labels":{"beta.kubernetes.io/arch":"amd64","beta.kubernetes.io/os":"linux","kubernetes.io/arch":"amd64","kubernetes.io/hostname":"minikube","kubernetes.io/os":"linux","minikube.k8s.io/commit":"f4b412861bb746be73053c9f6d2895f12cf78565","minikube.k8s.io/name":"minikube","minikube.k8s.io/primary":"true","minikube.k8s.io/updated_at":"","minikube.k8s.io/version":"v1.26.0","node-role.kubernetes.io/control-plane":"","node.kubernetes.io/exclude-from-external-load-balancers":""}},"timestamp":"","window":"1m0.147s","usage":{"cpu":"248760083n","memory":"1398756Ki"}}]}
```

### istio  

_Assumes istioctl matching the desired version of istio is installed locally. istio v1.14.1 is used for these examples._  

```bash
$ inv istio.add
$ inv istio.kiali
$ inv istio.tools    # prometheus, grafana, jaeger
```

### opa-istio-plugin (pending)  


## Invoke helper command

```bash
$ inv k8s.init <namespace> <domain>
```

If you are starting from a fresh launch of minikube, k8s.init will do the following:  

1. install metrics-service and kube-state-metrics
1. install istio
1. create <namespace>-local with istio-enabled annotations
1. create local Root CA certificates for local.<domain>
1. deploy the <domain> certs as secrets to istio-system
1. deploy `local-gateway` to istio, to accept traffic from [*].local.<domain>

You still need to add local host file DNS entries.  

## clean up

```bash
$ inv metrics.rm
$ inv istio.rm
$ inv dash.rm
$ inv ns.rm blue
$ inv domain.rm twdps.io
```

[Return](../README.md)
