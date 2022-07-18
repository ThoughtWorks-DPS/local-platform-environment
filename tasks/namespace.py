from invoke import task
from tasks.shared import is_local

CREATE_OPA_NAMESPACE="""
apiVersion: v1
kind: Namespace
metadata:
  name: {}-local
  labels:
    istio-injection: enabled
    opa-injection: enabled
"""

CREATE_NAMESPACE="""
apiVersion: v1
kind: Namespace
metadata:
  name: {}-local
  labels:
    istio-injection: enabled
"""

@task
def add(ctx, namespace, opa=None):
    """Create local instio-enabled namespace"""
    if is_local():
      if opa:
        print(f"Create namespace '{namespace}' with istio-injection and opa-injection enabled")
        ctx.run(f"echo '{CREATE_OPA_NAMESPACE.format(namespace)}' | kubectl apply -f - ")
      else:
        print(f"Create namespace '{namespace}' with istio-injection enabled")
        ctx.run(f"echo '{CREATE_NAMESPACE.format(namespace)}' | kubectl apply -f - ")

@task
def rm(ctx, namespace):
    """Delete local instio-enabled namespace"""
    if is_local():
      ctx.run(f"kubectl delete ns {namespace}-local")
