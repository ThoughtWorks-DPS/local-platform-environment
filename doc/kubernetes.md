## 3. Local Kubernetes install/setup (with userspace virtualization, on macos) 

Virtualization running in Userspace will consistently outperform full virtualization, all else being equal. RAM is a potentially critical requirement. (8gb at least in order to support istio.)  

• [minikube](https://minikube.sigs.k8s.io) on [hyperkit(https://github.com/moby/hyperkit)], or  

• [docker desktop](https://www.docker.com/products/docker-desktop) with kubernetes  

### minikube

• install hyperkit and minikube

_v1.23.0_ used for these examples.   

```bash
$ brew install hyperkit
$ brew install minikube
```

• configure minikube settings and start  

These are very performant config setting, but adjust to fit your development hardware.  

```bash
$ minikube config set vm-driver hyperkit
$ minikube config set memory 12288
$ minikube config set cpus 6
```

You can use the invoke helper script to start minikube wiith the following configuration:  
```bash
$ inv k8s.start
```

--insecure-registry "10.0.0.0/24"  
--addons registry  
--extra-config=kubelet.authentication-token-webhook=true   
--extra-config=kubelet.authorization-mode=Webhook  
--extra-config=scheduler.address=0.0.0.0  
--extra-config=controller-manager.address=0.0.0.0  

and this will run the minikbue registry network forwarder:  
```
$ docker run -d --rm -it --name=registry-fwd --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"
```

(_Use `minikube delete` to rermove the hyperkit vm and all configuration._)  

To remove the registry network forwarder use:
```
$ docker stop registry-fwd
```

### Local k8s security profile

To see how the default local development configuration compares to EKS using the CIS benchmark:  
```bash
$ inv k8s.bench
```

[Return](../README.md)
