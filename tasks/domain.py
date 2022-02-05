from invoke import task
from tasks.shared import is_local
      

CREATE_DOMAIN_GATEWAY="""
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: local-gateway
  namespace: istio-system
  labels:
    app: local-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 443
      name: https-local
      protocol: HTTPS
    tls:
      mode: SIMPLE
      credentialName: local.{0}-credential
    hosts:
    - "local.{0}"

"""

@task
def add(ctx, domain):
    """Create local dev namespace, deploy local gateway, and generate a valid cert for a local CA"""
    if is_local():
      ctx.run(f"mkcert -cert-file local.{domain}.crt -key-file local.{domain}.key local.{domain} \"*.local.{domain}\"")
      ctx.run(f"kubectl create -n istio-system secret tls local.{domain}-credential --key=local.{domain}.key --cert=local.{domain}.crt")
      ctx.run(f"echo '{CREATE_DOMAIN_GATEWAY.format(domain)}' | kubectl apply -f - ")
    
    
@task
def rm(ctx, domain):
    """rm local namespace, gateway, and certs"""
    if is_local():
      ctx.run(f"rm local.{domain}.crt local.{domain}.key")
      ctx.run(f"kubectl delete -n istio-system secret local.{domain}-credential")
      ctx.run(f"kubectl delete gateway local-gateway -n istio-system")

@task
def ls(ctx):
    """list namespaces, domains, and cert info for local k8s development configuration"""
    if is_local():
      ctx.run("echo GATEWAY && kubectl get gateways -n istio-system | grep 'local' && echo")
      ctx.run("echo CERT && kubectl get secrets -n istio-system | grep 'credential'")


@task
def cert(ctx,domain):
    """curl and display certificate information for provided domain"""
    ctx.run(f"curl -I -v --cacert local.{domain}.crt 'https://local.{domain}'")
