# Course Project Consortium Website

# Запуск

Команды из корня проекта в WSL. Для каждого релиза берите новый номер.

Скопировать настройки, затем заполнить `Backend/.env`:

```bash
cp -n Backend/.env.example Backend/.env
```

Тесты на отдельной PostgreSQL 17 (Python 3.12):

```bash
docker compose -f docker-compose.test.yml up --build --abort-on-container-exit --exit-code-from tests
docker compose -f docker-compose.test.yml down -v
```

Собрать релиз с новым номером (файл настроек содержит секреты):

```bash
export VERSION=v2
umask 077
mkdir -p releases
mkdir "releases/$VERSION" &&
docker compose -f docker-compose.build.yml build &&
docker compose --env-file Backend/.env -f docker-compose.yml config -o "releases/$VERSION/compose.yml"
```

Для пустой БД один раз создать таблицы:

```bash
docker compose -f releases/v2/compose.yml pull db
docker compose -f releases/v2/compose.yml up -d --pull never --wait db
docker compose -f releases/v2/compose.yml run --rm --no-deps --pull never --entrypoint flask web --app run.py init-db
```

Запустить релиз:

```bash
docker compose -f releases/v2/compose.yml up -d --no-build --pull never --scale web=2 --wait
```

Реплики: `docker compose -f releases/v2/compose.yml ps web`.

Сайт: http://localhost:3000. API и админка через Nginx: http://localhost:5000/api, http://localhost:5000/admin/. Второй порт задаёт `API_PORT`.

Логи: `docker compose -f releases/v2/compose.yml logs -f web frontend`.

Остановка: `docker compose -f releases/v2/compose.yml stop`.
