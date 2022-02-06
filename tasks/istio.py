from invoke import task
from tasks.shared import is_local


@task
def add(ctx):
    """deploy istio locally using istioctl"""
    if is_local():
      print("Use installed version of istiosctl to install to local cluster")
      ctx.run("istioctl install --set profile=default")
      

@task
def tools(ctx):
    """deploy prometheus, grafana, jaeger to local kubernetes"""
    if is_local():
      ctx.run("kubectl apply --recursive -f istiotools/install-jaeger.yaml")
      ctx.run("kubectl apply --recursive -f istiotools/install-prometheus.yaml")
      ctx.run("kubectl apply --recursive -f istiotools/install-grafana.yaml")

@task
def kiali(ctx):
    """deploy kiali"""
    if is_local():
      ctx.run("kubectl apply --recursive -f istiotools/install-kiali.yaml")

@task
def rm(ctx):
    """delete istio"""
    if is_local():
      ctx.run("kubectl delete --recursive -f istiotools/")
      ctx.run("istioctl x uninstall --purge")
      ctx.run("kubectl delete ns istio-system --grace-period=0 --force")
