from invoke import task
from tasks.shared import is_local


@task
def add(ctx):
    """deploy istio locally using istioctl and the istio operator"""
    if is_local():
      ctx.run("bash tasks/istio_manifest.sh")
      ctx.run("istioctl operator init && sleep 8")
      ctx.run("cat istiotools/istio-manifest.yaml | kubectl apply -f - ")
      

@task
def tools(ctx):
    """deploy prometheus, grafana, jaeger, kiali to local kubernetes"""
    KIALI_OPERATOR="""
helm install \
--set cr.create=true \
--set cr.namespace=istio-system \
--set spec.auth.strategy=anonymous \
--namespace kiali-operator \
--repo https://kiali.org/helm-charts \
kiali-operator kiali-operator  
"""
    if is_local():
      ctx.run("kubectl apply --recursive -f istiotools/")
      ctx.run(KIALI_OPERATOR)

@task
def rm(ctx):
    """delete istio"""
    if is_local():
      ctx.run("istioctl manifest generate | kubectl delete -f -")
      ctx.run("kubectl delete ns istio-system --grace-period=0 --force")
      ctx.run("kubectl delete ns istio-operator --grace-period=0 --force")
      ctx.run("kubectl delete ns kiali-operator --grace-period=0 --force")
      