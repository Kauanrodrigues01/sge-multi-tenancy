# SGE - Sistema de Gestão de Estoque

O **SGE (Sistema de Gestão de Estoque)** é uma solução completa para o gerenciamento de estoque. Ele oferece ferramentas para controlar produtos, fornecedores, marcas, categorias, entradas e saídas de estoque, com um sistema de notificações automáticas e insights baseados em inteligência artificial.

---

## **Principais Funcionalidades**
- **Gerenciamento de Estoque**:
  - Controle de produtos, fornecedores, marcas e categorias.
  - Registro de entradas e saídas de estoque.
  - Alertas automáticos de baixo estoque via WhatsApp e e-mail.
- **Integração com Inteligência Artificial**:
  - Sugestões de reposição com base em históricos de vendas e consumo.
  - Insights para otimização da gestão de estoque.
- **Gráficos e Métricas**:
  - Gráficos interativos usando Chart.js:
    - Valor de Vendas (últimos 7 dias).
    - Quantidade de Vendas Diárias (últimos 7 dias).
    - Distribuição de produtos por marca e categoria.
  - Métricas gerais:
    - **Produtos**: Quantidade total, custo total, preço de venda total, lucro total.
    - **Vendas**: Total de vendas, total de produtos vendidos, valor total de vendas, lucro total de vendas.
- **Estilização e Front-end**:
  - Design responsivo utilizando **Bootstrap**.
- **Notificações**:
  - Envio de mensagens automáticas via WhatsApp (API da **Evolution**).
  - Envio de e-mails com o próprio Django.
- **Automatização com Celery**:
  - **Tarefas agendadas** via Celery Beat para gerar relatórios diários sobre produtos, estoque e demanda.
  - Integração com **Gemini AI** para fornecer feedback automático baseado em análise de dados.

---

## **Tecnologias Utilizadas**
<p align="left">
  <img src="https://github.com/Kauanrodrigues01/Kauanrodrigues01/blob/main/icons/backend/python.svg" width="40" height="40" alt="Python" />
  <img src="https://github.com/Kauanrodrigues01/Kauanrodrigues01/blob/main/icons/backend/django.svg" height="50" alt="Django" />
  <img src="https://github.com/Kauanrodrigues01/Kauanrodrigues01/blob/main/icons/backend/postgresql-light.svg" width="40" height="40" alt="PostgreSQL" />
  <img src="https://github.com/Kauanrodrigues01/Kauanrodrigues01/blob/main/icons/frontend/bootstrap.svg" height="35" alt="BootStrap" />
  <img src="https://github.com/Kauanrodrigues01/Kauanrodrigues01/blob/main/icons/frontend/chartjs.svg" width="40" height="40" alt="ChartJS" />
</p>

- **Back-end**:
  - **Django** para criação do sistema web e gerenciamento do sistema e envio de e-mails.
  - Integração com a API da Evolution para envio de mensagens WhatsApp.
  - **Gemini** para integração de IA e fornecimento de insights.
  - **Celery e Celery Beat** para tarefas agendadas e processamento assíncrono.
- **Front-end**:
  - **Bootstrap** para estilização.
  - **Chart.js** para criação de gráficos interativos.

---

## **Como Rodar o Projeto com Docker**

### **1. Criar o Arquivo `.env`**
Antes de iniciar, crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```ini
# DJANGO SETTINGS
SECRET_KEY=django-insecure-h3y=dr4aic$ts$)z6_ngy%8!dkhd*n05l*wb1nwn+2ml&ep8qv
DEBUG=True
ALLOWED_HOSTS=*
LANGUAGE_CODE=pt-br
TIME_ZONE=America/Fortaleza

# INTEGRATION WITH GEMINI API
GEMINI_API_KEY=api-key
GEMINI_MODEL=gemini-1.5-flash

# INTEGRATION WITH EVOLUTION API
EVOLUTION_API_BASE_URL=http://localhost:8080/
EVOLUTION_API_TOKEN=api-token
MY_NUMBER=55*********
INSTANCE_NAME=test
INSTANCE_TOKEN=instance-token

# EMAIL
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=example@test.com
EMAIL_HOST_PASSWORD=@Test01020202010
MY_EMAIL=myemail@test.com

# URLS FOR DATABASE AND CELERY BROKER
DATABASE_URL=postgresql://myuser:mypassword@localhost:5432/mydatabase
CELERY_BROKER_URL=pyamqp://myuser:mypassword@localhost:5672/

# Credentials for superuser
SUPERUSER_USERNAME=admin
SUPERUSER_EMAIL=kauanrl09@gmail.com
SUPERUSER_PASSWORD=admin
```

### **2. Construir e Iniciar os Containers**

Execute os seguintes comandos para construir e iniciar os containers:

```bash
# Construir a imagem do projeto
$ docker compose build -t sge-app:0.0.1

# Iniciar os containers
$ docker compose up -d
```

Isso iniciará os seguintes serviços:
- **SGE App**: Aplicação Django
- **PostgreSQL**: Banco de dados
- **RabbitMQ**: Broker para Celery
- **Celery Worker**: Processamento assíncrono
- **Celery Beat**: Agendador de tarefas

Agora acesse: [http://localhost:8000/](http://localhost:8000/)

---

