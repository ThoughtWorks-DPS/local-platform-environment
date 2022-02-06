#!/bin/bash
set -e

latest=$(curl --silent "https://api.github.com/repos/kubernetes/kube-state-metrics/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/') 
curl -L https://api.github.com/repos/kubernetes/kube-state-metrics/zipball/${latest} --output ksm-${latest}.zip
unzip -u -j ksm-${latest}.zip "kubernetes-kube-state-metrics*/examples/standard/*" -d "metrics/kube-state-metrics"
kubectl apply --recursive -f metrics/kube-state-metrics/
rm ksm-${latest}.zip








