### 2. Local tools and setup

### Installing kubernetes locally  

It is recommended that you use either [minikube](https://minikube.sigs.k8s.io/docs/) or [Docker Desktop](https://www.docker.com/products/docker-desktop) as your local instance of kubernetes. The examples in this guide will use minikube.  

#### local kubernetes related packages used in this setup

[kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) • kubernetes api command-line tool  
[kubectx](https://github.com/ahmetb/kubectx) • cli to quickly swtich between local and remote k8s clusters  
[istioctl](https://istio.io) • istio command-line tool
[helm](https://helm.sh) • manage pod deploys  
[stern](https://github.com/wercker/stern)  • tails logs to the terminal from any number of local or remote pods  
[mkcert](https://github.com/FiloSottile/mkcert) • Automated management of certificates and CA for local https   
[skaffold](https://github.com/GoogleContainerTools/skaffold) • continuous development on local kubernetes  
[kubefwd](https://github.com/txn2/kubefwd) • develop locally with remotes services available as they would be in the remote cluster  
[krew](https://github.com/kubernetes-sigs/krew/) kubectl plugin manager, chiefly for cluster managers   
(_some useful plugins_)  
- _access-matrix_. Show an access matrix for server resources  
- _config-cleanup_. Automatically clean up your kubeconfig   
- _deprecations_. Compare a cluster against a specific version of k8s to reveal any deprecated uses  
- _evict-pod_. Evicts the given pod  
- _exec-as_. Like kubectl exec, but offers a `user` flag  
- _get-all_. Like 'kubectl get all', but everything  
- _images_. List detailed container information for a namespace  
- _konfig_. Merge and manage local kubeconfig*  
- _mtail_. Tail logs from multiple pods matching label*  
- _rbac-lookup_. Reverse lookup for RBAC  
- _rbac-view_. A tool to visualize your RBAC permissions  
- _resource-capacity_. Provides an overview of resource requests, limits, etc  
- _restart_. Restarts a pod with the given name*  
- _roll_. Rolling delete or targted namespaces pods*  
- _view-allocations_. Shows cluster cpu and memory allocations    
- _view-utilization_. Shows cluster cpu and memory utilization  
- _who-can_. like can-i but evaluates who at a permission level  

*installed by the setup script  

_code complete_  
[hadolint](https://github.com/hadolint/hadolint) • Dockerfile lint/inspection   
[kubeval](https://github.com/garethr/kubeval) • k8 yaml lint/inspection  
[git-secrets](https://github.com/awslabs/git-secrets)  

#### scripted setup

**helper scripts**  

Throughout this guide you will also see references to some helper scripts. Python `invoke` and related task files in this repository provide a convenient way to install the various services and examples. Use `invoke -l` to see a list of available shortcuts.  

There is a Pipfile that can be used in setting up a local python virtual environment.  

Scripts are provided that can accelerate the installation process for these tools.  

**install_mac.sh**  

Depends on the [homebrew](https://brew.sh) MacOS package manager.  

**install_windows.sh** (_pending_)  

### Honorable mentions for additional local customization  

You may enjoy using these tools.  

[oh-my-zsh](https://ohmyz.sh)  
[kube-ps1](https://github.com/jonmosco/kube-ps1)  

<p align="center"><img width="800" alt="oh-my-zsh with kube-ps1" src="oh-my-zsh-capture.png"></p>

[Return](../README.md)
