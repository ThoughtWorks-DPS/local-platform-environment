#!/usr/bin/env bash

export ISTIO_VERSION=$(istioctl version --remote=false)
echo "installing tools for istio version=${ISTIO_VERSION}"

# kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-${ISTIO_VERSION}/samples/addons/jaeger.yaml
# kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-${ISTIO_VERSION}/samples/addons/prometheus.yaml
# kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-${ISTIO_VERSION}/samples/addons/grafana.yaml

# kubectl create namespace kiali-operator
# helm install --set cr.create=true --set cr.namespace=istio-system --namespace kiali-operator --repo https://kiali.org/helm-charts kiali-operator kiali-operator
# sleep 20
# kubectl get secrets -o json -n istio-system | jq -r '.items[] | select(.metadata.name | test("kiali-service-account")).data.token' > kiali-token
# echo "token for current kiali instance running on minikube written to kiali-token"
# cat kiali-token
