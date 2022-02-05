
# Copyright 2016 The Kubernetes Authors. 
# with modifications
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# generate a local tag based on last SHA + random number
LASTSHA := $(shell git rev-parse HEAD | cut -c 1-8)
NEXTREVISION := $(shell expr $(shell helm history guestbook --namespace=blue-local --max=1 -o json | jq '.[].revision') + 1)
LOCALVERSION?=local.${LASTSHA}.${NEXTREVISION}

REGISTRY?=localhost:5000

release: clean build push clean

# builds a docker image that builds the app and packages it into a minimal docker image
local:
	docker build -t ${REGISTRY}/guestbook:${LOCALVERSION} .
	docker push ${REGISTRY}/guestbook:${LOCALVERSION}
	helm upgrade guestbook charts/guestbook --install --namespace=blue-local --set version=${LOCALVERSION}

# deploy docker registry credentials to kubernetes local development namespace
NAME="regcreds"
SERVER="docker.io"
NAMESPACE="blue-local"

regcreds:
	kubectl create secret docker-registry ${NAME} \
			--docker-server=${SERVER} \
			--docker-username=${DOCKER_USERNAME} \
			--docker-password=${DOCKER_PASSWORD} \
			--namespace=${NAMESPACE}

.PHONY: release clean build push local