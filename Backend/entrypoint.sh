#!/bin/bash

# Ожидание готовности PostgreSQL
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "db" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

# Запуск миграций и сидинга
python run.py --seed

# Запуск основного приложения
exec python run.py