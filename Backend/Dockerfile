
FROM tiangolo/uwsgi-nginx-flask:python3.12


COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt


COPY ./ ./

COPY nginx-logging.conf /etc/nginx/conf.d/logging.conf
