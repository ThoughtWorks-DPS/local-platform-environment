### 4. Deploy supporting services to kubernetes  

The python `invoke` files in this repository provide a convenient way to install the following services.  

• [metrics-server](https://github.com/kubernetes-incubator/metrics-server)  
• [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics)  
• [istio](https://istio.io)  
• open policy agent (pending)

_Use `invoke -l` to see a list of available shortcuts._  

### metric collectors 

• metrics-server (0.5.0)  
• kube-state-metrics (latest, v2.2.0)  

```bash
$ invoke metrics.add   
```

### istio  

_Assumes istioctl matching the designed version of istio is installed locally. istio v1.10.3 is used for these examples._  

```bash
$ inv istio.add
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
