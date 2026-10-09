# Запуск в minikube


```bash
docker version
minikube start --driver=docker
minikube update-context
minikube status
minikube kubectl -- get nodes
minikube kubectl -- get pods -A
```


## Развёртывание

```bash
alias kubectl='minikube kubectl --'
docker build -t consortium-backend:k8s1 Backend
docker build -t consortium-frontend:k8s1 my-app
minikube image load consortium-backend:k8s1
minikube image load consortium-frontend:k8s1
kubectl create secret generic backend-env --from-env-file=Backend/.env --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -f k8s/postgres.yaml
kubectl rollout status deployment/db --timeout=180s
kubectl apply -f k8s/init-db.yaml
kubectl wait --for=condition=complete job/init-db --timeout=180s
kubectl apply -f k8s/web.yaml -f k8s/frontend.yaml
kubectl rollout status deployment/web --timeout=180s
kubectl rollout status deployment/frontend --timeout=180s
kubectl get pods
```


```bash
minikube kubectl -- port-forward svc/frontend 3000:80
```


http://localhost:3000
`minikube kubectl -- -n course-video port-forward svc/frontend 3000:80`

## Масштабирование

```bash
minikube kubectl -- scale deployment/web --replicas=2
minikube kubectl -- scale deployment/frontend --replicas=2
minikube kubectl -- get pods
```
`-n course-video`