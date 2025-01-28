# FROM python:3.9-slim

# # Установить необходимые зависимости
# RUN apt-get update && apt-get install -y bash netcat && rm -rf /var/lib/apt/lists/*

# WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY . /app

# # Копируем и запускаем скрипт для заполнения базы данных
# COPY ./seed_authors.py /app/seed_authors.py
# RUN python /app/seed_authors.py

# COPY ./seed_magazines.py /app/seed_magazines.py
# RUN python /app/seed_magazines.py


# COPY ./seed_db.py /app/seed_db.py
# RUN python /app/seed_db.py

# COPY ./seed_projects.py /app/seed_projects.py
# RUN python /app/seed_projects.py

# COPY ./seed_news.py /app/seed_news.py
# RUN python /app/seed_news.py

# COPY ./seed_publications.py /app/seed_publications.py
# RUN python /app/seed_publications.py

# COPY ./seed_organisations.py /app/seed_organisations.py
# RUN python /app/seed_organisations.py

# COPY ./scripts/wait-for-it.sh /usr/local/bin/wait-for-it
# RUN chmod +x /usr/local/bin/wait-for-it

# CMD ["wait-for-it", "db:5432", "--", "python", "run.py"]


FROM python:3.9-slim

#RUN apt-get update && apt-get install -y bash netcat postgresql-client
RUN apt-get update && apt-get install -y bash netcat-openbsd postgresql-client
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Скрипт запуска
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
