from invoke import task
from tasks.shared import is_local


@task(optional=['tls'])
def deploy(ctx, tls=None):
    """httpbin ingress examples"""
    if is_local():
      ctx.run("kubectl apply -f examples/httpbin/deploy/httpbin-namespace.yaml")
      ctx.run("kubectl apply -f examples/httpbin/deploy --recursive")
      if tls:
        print('using tls')
        ctx.run('mkcert -cert-file local.httpbin.org.crt -key-file local.httpbin.org.key local.httpbin.org localhost 127.0.0.1 ::1')
        ctx.run('kubectl create -n istio-system secret tls httpbin-credential --key=local.httpbin.org.key --cert=local.httpbin.org.crt')
        ctx.run("kubectl apply -f examples/httpbin/tls --recursive")
      else:
        ctx.run("kubectl apply -f examples/httpbin/simple --recursive")


@task
def rm(ctx):
    """httpbin ingress examples"""
    if is_local():
      ctx.run("kubectl delete ns httpbin-local --grace-period=0 --force")
      ctx.run("kubectl delete secret -n istio-system httpbin-credential")
