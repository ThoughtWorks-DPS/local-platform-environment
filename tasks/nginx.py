from invoke import task
from tasks.shared import is_local

@task
def add(ctx):
    """nginx ingress examples"""
    if is_local():
      ctx.run('kubectl label namespace default istio-injection=enabled')
      ctx.run('mkcert -cert-file localhost.crt -key-file localhost.key localhost 127.0.0.1 ::1')
      ctx.run('kubectl create -n istio-system secret tls helloworld-localhost-credential --key=localhost.key --cert=localhost.crt')
      ctx.run("kubectl apply -f examples/nginx --recursive")
      


@task
def rm(ctx):
    """httpbin ingress examples"""
    if is_local():
      ctx.run("kubectl delete ns nginx-local --grace-period=0 --force")
      ctx.run("rm nginx.localhost.*")



# openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -subj "/O=$DOMAIN_NAME Inc./CN=$DOMAIN_NAME" -keyout $DOMAIN_NAME.key -out $DOMAIN_NAME.crt 
  
# #create the certificate signing request and the corresponding key
# openssl req -out helloworld.$DOMAIN_NAME.csr -newkey rsa:2048 -nodes -keyout helloworld.$DOMAIN_NAME.key -subj "/CN=helloworld.$DOMAIN_NAME/O=hello world from $DOMAIN_NAME"

# #using the certificate authority and it's key as well as the certificate signing requests, we can create our own self-signed certificate
# openssl x509 -req -days 365 -CA $DOMAIN_NAME.crt -CAkey $DOMAIN_NAME.key -set_serial 0 -in helloworld.$DOMAIN_NAME.csr -out helloworld.$DOMAIN_NAME.crt

# #Now that we have the certificate and the correspondig key we can create a Kubernetes secret to store them in our cluster.
# #We will create the secret in the istio-system namespace and reference it from the Gateway resource:
# kubectl create -n istio-system secret tls helloworld-localhost-credential --key=helloworld.localhost.key --cert=helloworld.localhost.crt