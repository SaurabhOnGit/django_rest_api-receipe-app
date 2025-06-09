FROM python:3.13.4-alpine3.21
LABEL maintainer="kunwarsaurabh"

ENV PYTHONBUFFEREDENCODING=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

COPY ./app /app
WORKDIR /app

EXPOSE 8000

ARG DEV=false

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # Install dependencies from requirements.txt
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then \
        /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /tmp/* && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PYTH='/py/bin:$PATH'


USER django-user
