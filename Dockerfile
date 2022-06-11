FROM python:3.8

COPY ./app /app
COPY ./app/requirements.txt /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 7000




