# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    pip3 install Flask && \
    pip3 install mysql-connector-python
COPY . .
CMD python3 app.py