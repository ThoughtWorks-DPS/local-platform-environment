## Example: nginx

The Apple Silicon architecture creates some challenges since both the local kubernetes installation and all pods deployed locally must have an arm64 arch version of each image deployed.  

### Alternative kubernetes deployment

This example will use k3d as the local kubernetes installation. You can install k3d using homebrew.  

```bash
brew install k3d
```

Launch a k3d single node cluster.  
```bash
k3d cluster create local-cluster --servers 1 --agents 1 --api-port 6443 --k3s-arg "--disable=traefik@server:0" \
    --port 8080:80@loadbalancer --port 8443:443@loadbalancer --agents-memory=8G
```

Confirm istioctl version 1.15.0 (istio has arm versions of all components starting with 1.15).  

```bash
istioctl version --remote=false
```

Deploy istio.  
```bash
inv istio.add
```

Deploy nginx example.  
```bash
inv nginx.add
```

You should now be able to reach the nginx entry point on both these urls:  

http://localhost:8080  
https://localhost:8443   # with expected 'self-signed cert' browser error  
