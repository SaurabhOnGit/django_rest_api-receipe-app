FROM python:3.13.4-alpine3.22
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

RUN python -m venv /py
RUN /py/bin/pip install --upgrade pip
RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev


RUN /py/bin/pip install -r /tmp/requirements.txt

RUN if [ "$DEV" = "true" ]; then \
        /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi
    # pip install --no-cache-dir -r /tmp/requirements.txt && \
RUN rm -rf /tmp && \
    apk del .tmp-build-deps

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"
# ENV PYTH='/py/bin:$PATH'

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

USER django-user
