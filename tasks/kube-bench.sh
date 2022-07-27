#!/usr/bin/env bash
kubectl apply -n default -f kube-bench/kube-bench-job.yaml && sleep 10

kubectl logs -n default -f job.batch/kube-bench --all-containers=true > bench.results
echo "kube-bench conformance results error:"
cat bench.results

kubectl delete -n default -f kube-bench/kube-bench-job.yaml
