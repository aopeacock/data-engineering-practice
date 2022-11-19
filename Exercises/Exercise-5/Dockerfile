FROM postgres:latest
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=postgres
COPY DDL_scripts.sql /docker-entrypoint-initdb.d/DDL_scripts.sql

FROM python:latest

WORKDIR /app
COPY . /app



RUN python3 -m pip install -r requirements.txt