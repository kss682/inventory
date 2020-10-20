FROM python:3.8.3-slim as base

COPY ./requirements.txt /build/requirements.txt
RUN pip install -r /build/requirements.txt

COPY ./api/ /build/api
