# Course Project Consortium Website

# Запуск

Команды из корня проекта в WSL. Для новой версии замените `v1` на `v2`.

Скопировать настройки, затем заполнить `Backend/.env`:

```bash
cp -n Backend/.env.example Backend/.env
```

Собрать образы:

```bash
VERSION=v1 docker compose -f docker-compose.build.yml build
```

Сохранить конфигурацию релиза (содержит секреты):

```bash
umask 077
mkdir -p releases
mkdir releases/v1 &&
VERSION=v1 docker compose --env-file Backend/.env -f docker-compose.yml config -o releases/v1/compose.yml
```

Для пустой БД один раз создать таблицы:

```bash
docker compose -f releases/v1/compose.yml pull db
docker compose -f releases/v1/compose.yml up -d --pull never --wait db
docker compose -f releases/v1/compose.yml run --rm --no-deps --pull never --entrypoint flask web --app run.py init-db
```

Запустить релиз:

```bash
docker compose -f releases/v1/compose.yml up -d --no-build --pull never --wait
```

Сайт: http://localhost:3000. API: http://localhost:5000/api. Админка: http://localhost:5000/admin/.

Логи: `docker compose -f releases/v1/compose.yml logs -f web frontend`.

Остановка: `docker compose -f releases/v1/compose.yml stop`.
