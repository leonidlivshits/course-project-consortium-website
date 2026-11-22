#!/usr/bin/env bash
set -euo pipefail

route=${1:-}
case "$route" in
  rolling|blue|green|canary-90-10|canary-50-50|canary-0-100|ab|shadow) ;;
  *) printf 'Укажи маршрут из папки routes.\n' >&2; exit 1 ;;
esac

profile=${DEPLOY_PROFILE:-minikube}
k() { minikube -p "$profile" kubectl -- --context="$profile" -n default "$@"; }

resource=httproute/consortium-api
k apply -f "$(dirname "$0")/routes/$route.yaml"
generation=$(k get "$resource" -o jsonpath='{.metadata.generation}')
for condition in Accepted ResolvedRefs; do
  field=".status.parents[0].conditions[?(@.type==\"$condition\")]"
  k wait "$resource" --for="jsonpath={$field.observedGeneration}=$generation" --timeout=45s
  k wait "$resource" --for="jsonpath={$field.status}=True" --timeout=45s
done

url=${DEPLOY_URL:-http://127.0.0.1:18880}
deadline=$((SECONDS + 30))
while ((SECONDS < deadline)); do
  if response=$(curl -s --max-time 2 -o /dev/null \
      -w '%{http_code} %header{x-demo-route}' "$url/api/live") &&
      [[ $response == "204 $route" ]]; then
    printf 'Envoy применил маршрут %s.\n' "$route"
    exit 0
  fi
  sleep 0.5
done

printf 'Envoy не подтвердил маршрут %s через %s. Последний ответ: %s\n' "$route" "$url" "${response:-нет}" >&2
exit 1
