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
  - **Django** para o criação do sistema web e gerenciamento do sistema e envio de e-mails.
  - Integração com a API da Evolution para envio de mensagens WhatsApp.
  - **Gemini** para integração de IA e fornecimento de insights.
- **Front-end**:
  - **Bootstrap** para estilização.
  - **Chart.js** para criação de gráficos interativos.

---

## **Integrações**

<img src="https://github.com/Kauanrodrigues01/Kauanrodrigues01/blob/main/images/evolution-api.png" width="180" alt="Evolution API" />

- Envio de mensagens automáticas pelo WhatsApp.
- Alertas de movimentações e baixo estoque.

<img src="https://github.com/Kauanrodrigues01/Kauanrodrigues01/blob/main/images/gemini.png" width="150" alt="Evolution API" />

- IA para sugestões de reposição e insights de otimização.

---

## **Visualização do Sistema**

### **Gráficos**

- **Valor de Vendas (últimos 7 dias):**
- **Quantidade de Vendas Diárias (últimos 7 dias):**
- **Produtos por Marca:**
- **Produtos por Categoria:**

> *Adicionar aqui imagens de exemplos de gráficos gerados.*

### **Métricas**

- **Produtos**:
  - Quantidade Total: `total_quantity`
  - Custo Total: `total_cost_price`
  - Preço de Venda Total: `total_selling_price`
  - Lucro Total: `total_profit`
- **Vendas**:
  - Total de Vendas: `total_sales`
  - Total de Produtos Vendidos: `total_products_sold`
  - Valor Total de Vendas: `total_sales_value`
  - Lucro Total de Vendas: `total_sales_profit`

> *Adicionar aqui imagens de exemplos de visualização de métricas.*

---

## **Como Configurar o Projeto**

### **Pré-requisitos**
1. Python 3.10+
2. Django 4.2+
4. Conta na API da Evolution(Caso não houver, o projeto vai funcionar normalmente, mas sem o envio de notificações pelo Whatssap)
5. Configuração do Gemini para integração de IA

### **Instalação**
```bash
# Clone o repositório
$ git clone https://github.com/seuprojeto/sge.git

# Acesse a pasta do projeto
$ cd sge

# Configurar variáveis de ambiente

# Instale as dependências Python
$ pip install -r requirements.txt

# Realize as migrações
$ python manage.py migrate

# Inicie o servidor
$ python manage.py runserver
```
