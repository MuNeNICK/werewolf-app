FROM python:3.9.7-slim-buster

WORKDIR /usr/src/app
ENV FLASK_APP=app

COPY /backend/requirements.txt ./

RUN apt-get update && apt-get install python-dev python3-dev default-libmysqlclient-dev default-mysql-client build-essential -y

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD backend/entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]