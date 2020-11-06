# COMPILE IMAGE
FROM python:3.8.2-alpine AS compile-image
LABEL maintainer="green2cerberuz@gmail.com"

WORKDIR /opt/app

RUN apk add --no-cache python3-dev postgresql-dev binutils

# Install pipenv
RUN pip3 install pipenv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" VIRTUAL_ENV="/opt/venv"

COPY ./provision/requirements.txt .
RUN pip install -r requirements.txt

# RUNTIME IMAGE
FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10 AS runtime-image

# Copy virtual environment and set PATH
COPY --from=compile-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN apk add postgresql-dev curl && rm -r -f /var/cache/apk/*

ENV APP_HOME /usr/src/
COPY ./src $APP_HOME
WORKDIR $APP_HOME

