#!/bin/sh

set -e

echo "[*] nerdctl build start"
nerdctl -n k8s.io build -t localhost/metric-python-test:alpha .
echo "[*] nerdctl build done"

echo "[*] deploy start"
kubectl apply -f ./cicd/deploy.yaml
echo "[*] deploy done"
