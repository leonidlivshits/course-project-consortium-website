FROM python:3.9-slim

# Установить необходимые зависимости
RUN apt-get update && apt-get install -y bash netcat && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

COPY ./scripts/wait-for-it.sh /usr/local/bin/wait-for-it
RUN chmod +x /usr/local/bin/wait-for-it

CMD ["wait-for-it", "db:5432", "--", "python", "run.py"]






# FROM python:3.9-slim
# ENV PYTHONPATH=/app

# WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# #COPY . .
# COPY . /app
# #WORKDIR /app

# CMD ["python", "run.py"]