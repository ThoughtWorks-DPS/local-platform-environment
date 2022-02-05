"""shared functions"""
import os, sys

CONTEXT_MINIKUBE="minikube"
CONTEXT_DOCKER_FOR_MAC="docker-for-mac"
cmd="kubectl config current-context"

def is_local():
    """sys.exit if not using current-context of minikube or docker-for-mac"""
    result = os.popen(cmd).read().rstrip()
    if result!=CONTEXT_MINIKUBE and result!=CONTEXT_DOCKER_FOR_MAC:
      #print('err: these shortcuts for local kubernetes only')
      sys.exit('err: these shortcuts for local kubernetes only')
    return True