# FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
# RUN apk --update add bash nano
# ENV STATIC_URL /static
# ENV STATIC_PATH /var/www/app/static
# COPY ./requirements.txt /var/www/requirements.txt
# RUN pip install -r /var/www/requirements.txt

# FROM python:3.11
# COPY ./requirements.txt /var/www/requirements.txt
# RUN pip install -r /var/www/requirements.txt

# metric_service/start.sh
# #!/bin/bash
# app="docker.test"
# docker build -t ${app} .
# docker run -d -p 56733:80 \
#   --name=${app} \
#   -v $PWD:/app ${app}


# FROM python:3.9.10-alpine3.14
# WORKDIR /srv
# RUN pip install --upgrade pip
# RUN pip install flask
# COPY . /srv
# ENV FLASK_APP=app
# CMD ["python","app.py"]



FROM python:3.8

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py ./

# EXPOSE 5000

CMD ["python", "app.py"]

# FROM python:3.9.10-alpine3.14
# WORKDIR /srv
# RUN pip install --upgrade pip
# RUN pip install flask
# COPY . /srv
# ENV FLASK_APP=app
# CMD ["python","app.py"]