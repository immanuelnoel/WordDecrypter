FROM python:3.7-alpine

RUN apk add --update-cache \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install pyspellchecker \
  && rm -rf /var/cache/apk/*

WORKDIR /src