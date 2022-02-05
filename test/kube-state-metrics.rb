# frozen_string_literal: true

require 'inspec'

JSONPATH='{.items[*].status.conditions[?(@.type=="Ready")].status}'

describe command("kubectl get pods -l app.kubernetes.io/name=kube-state-metrics --namespace=kube-system -o=jsonpath='#{JSONPATH}'") do
  its('exit_status') { should eq 0 }
  its('stderr') { should cmp '' }
  its('stdout') { should match /^True/ }
  its('stdout') { should_not match /False/ }
end