### 5. Local kubernetes observability

#### Istio observability tools  

To install the istio-integrated tools: (prometheus, grafana, jeager, and kiali locally)
```bash
$ inv istio.tools
```

$ istioctl dashboard grafana  
$ istioctl dashboard kiali  
$ istioctl dashbaord jaeger  
$ istioctl dashboard prometheus  

#### kubernetes Dashboard  

While use of the kubernetes dashboard generally is not recommended, it may of course be deployed locally should you prefer.  

```bash
$ inv dash.add  # v2.0.5 
```

Once the install is completed, the above invoke command will proxy the dashboard interface, launching a browser and place the require token into the clipboard.  

The browser windows will appear. Select the `token` authentication method and Ctrl-V to paste the admin-user token in your clipboard. (You will receive a 'unsigned' cert error message.)  

To fetch local kubernetes-dashboard user token to the clipboard again:  
```bash
$ inv dash.token
```

To reset the dashboard port forwarder:  
```bash
$ inv dash.reset
```

#### Logs  

[Using](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs) kubectl to view individual pod logs.  

[stern](https://github.com/wercker/stern): Multi pod and container log tailing for Kubernetes.  

Logs can also be viewed through the kubernetes dashboard.  

[Return](../README.md)  
