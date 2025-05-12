#!/bin/bash

export RUNNER_REPO=$(yq -r ".runners.spec.template.spec.repo" secrets.yaml)
export RUNNER_METADATA=$(yq -r ".runners.metadata.name" secrets.yaml)
export RUNNER_NS=$(yq -r ".runners.name" secrets.yaml)

echo $RUNNER_REPO
echo $RUNNER_METADATA
echo $RUNNER_NS


cat << EOF | kubectl apply -n $RUNNER_NS -f -
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: $RUNNER_METADATA
spec:
  replicas: 1
  template:
    spec:
      repository: $RUNNER_REPO
EOF