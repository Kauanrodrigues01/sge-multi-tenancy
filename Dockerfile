# Description: Dockerfile to build a Django image using Alpine Linux as base image.
FROM python:3.13-alpine AS builder

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev && \
    pip install --no-cache -r requirements.txt && \
    find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + && \
    runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" && \
    apk add --virtual .rundeps $runDeps && \
    apk del .build-deps


# Now multistage build
FROM python:3.13-alpine

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

RUN adduser -h /app -s /bin/sh -D userapp

WORKDIR /app

COPY . .

RUN apk add --no-cache curl && \
    find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + && \
        runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
        )" && \
    apk add --virtual .rundeps $runDeps

RUN chown userapp:userapp /app && \
    mkdir -p /app/static && \
    chmod -R 777 /app/static && \
    mkdir -p /app/uwsgi && \
    chmod -R 777 /app/uwsgi


ENV SECRET_KEY=django-insecure-h3y=dr4aic$ts$)z6_ngy%8!dkhd*n05l*wb1nwn+2ml&ep8qv \
    DEBUG=True \
    ALLOWED_HOSTS=* \
    LANGUAGE_CODE=pt-br \
    TIME_ZONE=America/Fortaleza

EXPOSE 8000

USER userapp