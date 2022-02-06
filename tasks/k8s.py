from invoke import task
from tasks.shared import is_local
from tasks import metrics
from tasks import istio
from tasks import dashboard
from tasks import domain
from tasks import namespace

@task
def start(ctx):
    """start minikube with extra-config values and tunnel lb"""
    START_K8S="""
minikube start \
--container-runtime=containerd \
--insecure-registry "10.0.0.0/24" \
--addons registry \
--extra-config=kubelet.authentication-token-webhook=true \
--extra-config=kubelet.authorization-mode=Webhook \
--extra-config=scheduler.address=0.0.0.0 \
--extra-config=controller-manager.address=0.0.0.0
"""
    ctx.run(START_K8S)
    ctx.run("docker run -d --rm -it --name=registry-fwd --network=host alpine ash -c \"apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000\"")
    ctx.run('minikube tunnel &')

@task
def init(ctx, localns, localdomain):
    """deploy locally metrics apis, istio, create specified local namespace and domain ingress"""
    if is_local():
      metrics.add(ctx)
      istio.add(ctx)
      namespace.add(ctx, localns)
      domain.add(ctx, localdomain)

@task
def bench(ctx):
    """Display results from kube-bench run against local cluster"""
    if is_local():
      ctx.run('bash tasks/kube-bench.sh')

@task
def reset(ctx):
    """Delete and restart minikube and local registry"""
    if is_local():
      rm(ctx)
      start(ctx)

@task
def rm(ctx):
    """delete current minikube vm instance and stop local registry"""
    if is_local():
      ctx.run('docker stop registry-fwd')
      ctx.run('minikube delete')
