# frozen_string_literal: true

require 'inspec'

JSONPATH='{.items[*].status.conditions[?(@.type=="Ready")].status}'

describe command("kubectl get pods -l k8s-app=metrics-server --namespace=kube-system -o=jsonpath='#{JSONPATH}'") do
  its('exit_status') { should eq 0 }
  its('stderr') { should cmp '' }
  its('stdout') { should match /^True/ }
  its('stdout') { should_not match /False/ }
end

describe command("kubectl get --raw \"/apis/metrics.k8s.io/v1beta1/nodes\"") do
  its('exit_status') { should eq 0 }
  its('stderr') { should cmp '' }
  its('stdout') { should include ("\"kind\":\"NodeMetricsList\"") }
end
