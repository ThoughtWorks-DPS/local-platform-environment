from invoke import task
from tasks.shared import is_local


@task
def deploy(ctx):
    if is_local():
      ctx.run("kubectl delete -f bookinfo --recursive")
