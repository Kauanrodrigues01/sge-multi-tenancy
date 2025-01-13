# Utilizando a imagem do Python
FROM python:3.12-slim

WORKDIR /sge

COPY . .

RUN apt-get update && \
    apt-get install -y gcc pkg-config && \
    rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip
RUN pip install -r requirements_dev.txt
RUN python3 manage.py migrate --no-input
RUN python3 manage.py collectstatic --no-input

EXPOSE 8000

# Definir o comando para iniciar a aplicação com uWSGI
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
