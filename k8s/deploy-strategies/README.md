# Стратегии развёртывания

```bash
minikube start --driver=docker
k() { minikube kubectl -- -n default "$@"; }
d=k8s/deploy-strategies

for version in v1 v2; do
  docker build --build-arg APP_VERSION="$version" -t "consortium-backend:deploy-$version" Backend
  minikube image load "consortium-backend:deploy-$version" --overwrite=true
done

minikube kubectl -- apply --server-side -f https://github.com/envoyproxy/gateway/releases/download/v1.10.0/install.yaml
minikube kubectl -- -n envoy-gateway-system rollout status deployment/envoy-gateway --timeout=300s
k apply -f "$d/gateway.yaml"
k wait --for=condition=Accepted gateway/consortium --timeout=180s
k apply -k "$d/rolling"
k rollout status deployment/web --timeout=180s
```

Проброс порта

```bash
eg() { minikube kubectl -- -n envoy-gateway-system "$@"; }
selector=gateway.envoyproxy.io/owning-gateway-namespace=default,gateway.envoyproxy.io/owning-gateway-name=consortium
eg wait --for=condition=Available deployment -l "$selector" --timeout=180s
svc=$(eg get svc -l "$selector" -o jsonpath='{.items[0].metadata.name}')
eg port-forward "svc/$svc" 18880:80
```

в первом терминале

```bash
switch() { bash "$d/route.sh" "$1" && export TRAFFIC_ROUTE="$1"; }
traffic() { bash "$d/traffic.sh" "$@"; }
sample() {
  local responses
  responses=$(traffic "$@") || return
  awk '{print $2, $3}' <<< "$responses" | sort | uniq -c
}
switch rolling
```

## Rolling

```bash
traffic 6
TRAFFIC_DELAY=0.5 traffic 90 &
sender=$!
k set image deployment/web web=consortium-backend:deploy-v2
k rollout status deployment/web --timeout=180s
wait "$sender"
k get pods -l app=web
```

## Blue/Green

```bash
k apply -k "$d/v1"
k apply -k "$d/v2"
k rollout status deployment/web-v1 --timeout=180s
k rollout status deployment/web-v2 --timeout=180s

switch blue && sample 20
switch green && sample 20
switch blue && sample 20
```

## Canary

```bash
switch canary-90-10 && sample 200
switch canary-50-50 && sample 200
switch canary-0-100 && sample 200
```

## A/B

```bash
switch ab && sample 20 && sample 20 -H 'X-User-Group: beta'
```

## Shadow

```bash
switch shadow && start=$(date -u +%Y-%m-%dT%H:%M:%S.%NZ) && traffic 6
k logs -l app=web-v2 --prefix --since-time="$start" --tail=-1 | grep -F '"http.route": "/api/news"'
```

## Возврат на web

```bash
switch rolling
```
