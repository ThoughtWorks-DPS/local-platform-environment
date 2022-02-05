from invoke import task
from tasks.shared import is_local

@task
def add(ctx):
    """deploy locally metrics-server and kube-state-metrics apis"""
    if is_local():
      ctx.run('kubectl apply -f metrics/metrics-server --recursive')
      ctx.run('bash tasks/install_ksm.sh')

@task
def rm(ctx):
    """delete metrics apis"""
    if is_local():
      ctx.run('kubectl delete -f metrics/ --recursive')
