#!/usr/bin/env bash
set -euo pipefail

count=${1:-1}
if (($#)); then
  shift
fi
if [[ ! $count =~ ^[1-9][0-9]*$ ]]; then
  printf 'Укажи положительное число запросов.\n' >&2
  exit 1
fi

for ((i=0; i<count; i++)); do
  response=$(curl -sS --max-time 5 -o /dev/null \
    -w '%{http_code} %header{x-app-version} %header{x-app-pod} %header{x-demo-route}' \
    "$@" "${DEPLOY_URL:-http://127.0.0.1:18880}/api/news")
  read -r status version pod route <<< "$response"
  printf '%s %s %s %s\n' "$(date +%T)" "$status" "$version" "$pod"
  if [[ $status != 200 || $version != v[12] || -z $pod ]]; then
    printf 'Получен неожиданный ответ: %s\n' "$response" >&2
    exit 1
  fi
  if [[ -n ${TRAFFIC_ROUTE:-} && $route != "$TRAFFIC_ROUTE" ]]; then
    printf 'Ожидался маршрут %s, ответил %s.\n' "$TRAFFIC_ROUTE" "$route" >&2
    exit 1
  fi
  sleep "${TRAFFIC_DELAY:-0}"
done
