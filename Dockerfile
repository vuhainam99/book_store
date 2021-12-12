FROM python:3.8.3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GRPC_PYTHON_BUILD_SYSTEM_OPENSSL 1
ENV GRPC_PYTHON_BUILD_SYSTEM_ZLIB 1

RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/

COPY . ./

RUN apk update \
    && apk add --no-cache gcc g++ \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev cargo jpeg-dev zlib-dev libpq


RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt


ENV PATH="/py/bin:$PATH"