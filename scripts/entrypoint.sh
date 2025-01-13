#!/bin/bash

set -e

# Realizar as migrações do banco de dados
python manage.py migrate --no-input
echo "COLETANDO ARQUIVOS ESTATICOS"

# Coletar os arquivos estáticos
python manage.py collectstatic --no-input
echo "APLICANDO MIGRACOES"

# Iniciar o servidor uWSGI
uwsgi --http :8000 --module app.wsgi --chmod-socket=666 --master --enable-threads --processes 2 --threads 4 --static-map /static=/sge/static
echo "SERVIDOR INICIADO"
