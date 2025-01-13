#!/bin/bash

# Realizar as migrações do banco de dados
python3 manage.py migrate --no-input

# Coletar os arquivos estáticos
python3 manage.py collectstatic --no-input

# Iniciar o servidor uWSGI
uwsgi --http :8000 --module app.wsgi --chmod-socket=666 --master --enable-threads --processes 2 --threads 4 --static-map /static=/sge/static
