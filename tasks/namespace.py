from invoke import task
from tasks.shared import is_local

CREATE_NAMESPACE="""
apiVersion: v1
kind: Namespace
metadata:
  name: {}-local
  labels:
    istio-injection: enabled
"""

@task
def add(ctx, namespace):
    """Create local instio-enabled namespace"""
    if is_local():
      ctx.run(f"echo '{CREATE_NAMESPACE.format(namespace)}' | kubectl apply -f - ")

@task
def rm(ctx, namespace):
    """Delete local instio-enabled namespace"""
    if is_local():
      ctx.run(f"kubectl delete ns {namespace}-local")