# Course Project Consortium Website

Flask API, React frontend и PostgreSQL. Запуск из корня репозитория в WSL с Docker Desktop:

```bash
cp -n Backend/.env.example Backend/.env
cp -n my-app/.env.example my-app/.env
docker compose --env-file Backend/.env up -d --wait db
docker compose --env-file Backend/.env up -d --build web frontend
```

Сайт: http://localhost:3000, API: http://localhost:5000/api. Логи: `docker compose --env-file Backend/.env logs -f web frontend`. Остановка: `docker compose --env-file Backend/.env stop`.
