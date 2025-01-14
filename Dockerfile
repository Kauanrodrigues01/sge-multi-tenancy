FROM python:3.13-slim

WORKDIR /sge

COPY . .

RUN apt-get update && \
    apt-get install -y gcc build-essential libpq-dev libpcre3-dev make libc-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod -R +x /sge/scripts
RUN groupadd -r usergroup && useradd -r -g usergroup -m user
RUN chown -R user:usergroup /sge

# Garantir permissões adequadas para o diretório
RUN chmod -R 755 /sge
RUN mkdir -p /sge/static && chown -R user:usergroup /sge/static && chmod -R 755 /sge/static

USER user

EXPOSE 8000

ENTRYPOINT ["/bin/sh", "/sge/scripts/entrypoint.sh"]