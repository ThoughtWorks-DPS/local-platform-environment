from invoke import task
from subprocess import run, PIPE
import os
from tasks.shared import is_local


@task
def add(ctx):
    """deploy locally kubernetes dashboard"""
    if is_local():
      ctx.run("kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/aio/deploy/recommended.yaml")
      ctx.run("kubectl apply -f dashboard/dashboard-admin-user.yaml")
      p = run("kubectl -n kubernetes-dashboard describe secret admin-user | awk '{for(i=1;i<=NF;i++) {if($i~/token:/) print $(i+1)}}'", shell=True, stdout=PIPE, encoding='ascii')
      cmd = "echo \"{}\" | pbcopy".format(p.stdout)
      ctx.run(cmd)
      print('dashboard token copied to clipboard')
      dashboard = 'kubectl proxy &'
      os.system(dashboard)
      ctx.run("open http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/")


@task
def token(ctx):
    """copy dashboard token to clipboard"""
    if is_local():
      p = run("kubectl -n kubernetes-dashboard describe secret admin-user | awk '{for(i=1;i<=NF;i++) {if($i~/token:/) print $(i+1)}}'", shell=True, stdout=PIPE, encoding='ascii')
      print(p.stdout)
      cmd = "echo \"{}\" | pbcopy".format(p.stdout)
      ctx.run(cmd)
      print('dashboard token copied to clipboard')


@task
def reset(ctx):
    """reset dashboard proxy"""
    if is_local():
      ctx.run('pkill kubectl')
      p = run("kubectl -n kubernetes-dashboard describe secret admin-user | awk '{for(i=1;i<=NF;i++) {if($i~/token:/) print $(i+1)}}'", shell=True, stdout=PIPE, encoding='ascii')
      cmd = "echo \"{}\" | pbcopy".format(p.stdout)
      ctx.run(cmd)
      print('dashboard token copied to clipboard')
      dashboard = 'kubectl proxy &'
      os.system(dashboard)
      ctx.run("open http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/")


@task
def rm(ctx):
    """delete dashboard"""
    if is_local():
      ctx.run('pkill kubectl')
      ctx.run("kubectl delete ns kubernetes-dashboard --grace-period=0 --force")
      