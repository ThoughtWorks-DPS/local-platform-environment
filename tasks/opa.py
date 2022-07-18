from invoke import task
from tasks.shared import is_local

@task
def ns(ctx):
    """update httpbin-local namespace"""
    if is_local():
      ctx.run("kubectl apply -f examples/opa/httpbin-local-additions --recursive")

@task
def slp(ctx):
    """deploy SLP"""
    if is_local():
      ctx.run("kubectl apply -f examples/opa/opa-namespace.yaml")
      ctx.run("kubectl apply -f examples/opa/deploy-slp --recursive")

@task
def ac(ctx):
    """deploy admission controller"""
    if is_local():
      ctx.run("kubectl apply -f examples/opa/deploy-admission-controller --recursive")


@task
def restart(ctx):
    """opa examples"""
    if is_local():
      ctx.run("kubectl delete -f examples/httpbin/deploy/httpbin-deployment.yaml & sleep 5")
      ctx.run("kubectl apply -f examples/httpbin/deploy/httpbin-deployment.yaml")

@task
def rm(ctx):
    """httpbin ingress examples"""
    if is_local():
      ctx.run("kubectl delete ns httpbin-local --grace-period=0 --force")
      ctx.run("kubectl delete ns opa-istio --grace-period=0 --force")
