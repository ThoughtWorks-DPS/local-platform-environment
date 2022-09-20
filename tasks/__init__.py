from invoke import Collection

from tasks import k8s
from tasks import istio
from tasks import dashboard
from tasks import httpbin
from tasks import domain
from tasks import namespace
from tasks import opa
from tasks import nginx

ns = Collection()

ns.add_collection(k8s)
ns.add_collection(istio)
ns.add_collection(dashboard, name='dash')
ns.add_collection(httpbin)
ns.add_collection(domain)
ns.add_collection(namespace, name="ns")
ns.add_collection(opa)
ns.add_collection(nginx)
