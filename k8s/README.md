# Запуск в minikube


```bash
docker version
minikube start --driver=docker
minikube update-context
minikube status
minikube kubectl -- get nodes
minikube kubectl -- get pods -A
```


## Первый запуск в новом кластере

```bash
alias kubectl='minikube kubectl --'
docker build -t consortium-backend:k8s2 Backend
docker build -t consortium-frontend:k8s1 my-app
minikube image load consortium-backend:k8s2
minikube image load consortium-frontend:k8s1
kubectl create secret generic backend-env --from-env-file=Backend/.env --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -f k8s/postgres.yaml
kubectl rollout status deployment/db --timeout=180s
kubectl apply -f k8s/init-db.yaml
kubectl wait --for=condition=complete job/init-db --timeout=180s
kubectl apply -f k8s/frontend-nginx.yaml -f k8s/web.yaml -f k8s/frontend.yaml
kubectl rollout status deployment/web --timeout=180s
kubectl rollout status deployment/frontend --timeout=180s
kubectl get pods
```


```bash
minikube kubectl -- port-forward svc/frontend 3000:80
```


http://localhost:3000

## Обновление

После изменения бэкенда:

```bash
docker build -t consortium-backend:k8s2 Backend
minikube image load consortium-backend:k8s2
minikube kubectl -- rollout restart deployment/web
minikube kubectl -- rollout status deployment/web --timeout=180s
```

После изменения `k8s/frontend-nginx.yaml`:

```bash
minikube kubectl -- apply -f k8s/frontend-nginx.yaml
minikube kubectl -- rollout restart deployment/frontend
minikube kubectl -- rollout status deployment/frontend --timeout=180s
```

## Масштабирование

```bash
minikube kubectl -- scale deployment/web --replicas=2
minikube kubectl -- scale deployment/frontend --replicas=2
minikube kubectl -- get pods
```

## Логи в VictoriaLogs

Helm: https://helm.sh/docs/intro/install/

```bash
export PATH="$HOME/.local/bin:$PATH"
helm repo add vm https://victoriametrics.github.io/helm-charts/ --force-update
helm upgrade --install vls vm/victoria-logs-single --version 0.13.10 -n logging --create-namespace -f k8s/victoria-logs-values.yaml --wait
helm upgrade --install collector vm/victoria-logs-collector --version 0.3.8 -n logging -f k8s/victoria-logs-collector-values.yaml --wait
minikube kubectl -- -n logging get pods
```

Интерфейс:

```bash
minikube kubectl -- -n logging port-forward svc/vls-victoria-logs-single-server 9428:9428
```

http://localhost:9428/select/vmui/
