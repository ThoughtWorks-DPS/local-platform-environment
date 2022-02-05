#!/bin/bash
set -e

# generate manifest for version of locally installed istioctl
version=$(istioctl version --remote=false)

cat << EOF > istiotools/istio-manifest.yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  namespace: istio-system
  name: istiocontrolplane
spec:
  profile: default
  tag: $version-distroless
  meshConfig:
    accessLogFile: /dev/stdout
    accessLogEncoding: JSON
    enableTracing: true
    defaultConfig:
      tracing:
        zipkin:
          address: "zipkin:9411"
  components:
    ingressGateways:
    - name: istio-ingressgateway
      enabled: true
      k8s:
        resources:
          limits:
            cpu: 250m
            memory: 256Mi
          requests:
            cpu: 100m
            memory: 128Mi
EOF



