# SGE Multi Tenancy - Sistema de Gestão de Estoque

<p align="center">
  <img src="https://raw.githubusercontent.com/Kauanrodrigues01/Kauanrodrigues01/refs/heads/main/images/projetos/sge/dashboard.png" alt="Dashboard" width="700"/>
</p>

O **SGE (Sistema de Gestão de Estoque)** é uma solução completa para o gerenciamento de estoque. Ele oferece ferramentas para controlar produtos, fornecedores, marcas, categorias, entradas e saídas de estoque, com um sistema de notificações automáticas e insights baseados em inteligência artificial. Foi programado para suportar múltiplos usuários com a separação de seus dados.

---

## **🔍 Menu de Navegação**
- [Principais Funcionalidades](#principais-funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Integrações](#integrações)
- [Visualização do Sistema](#visualizacao-do-sistema)
- [Como Configurar o Projeto](#como-configurar-o-projeto)
  - [Executando com Docker](#executando-com-docker)

---

<span id="principais-funcionalidades"></span>
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
- **Troca de Tema (Light/Dark):**
  - Alternância entre temas claro e escuro.
  - Preferência salva no localStorage do navegador para persistência entre sessões.

---

<span id="tecnologias-utilizadas"></span>
## **Tecnologias Utilizadas**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=Chart.js&logoColor=white)

- **Back-end**:
  - **Django** para o criação do sistema web e gerenciamento do sistema e envio de e-mails.
  - Integração com a API da Evolution para envio de mensagens WhatsApp.
  - **Gemini** para integração de IA e fornecimento de insights.
- **Front-end**:
  - **Bootstrap** para estilização.
  - **Chart.js** para criação de gráficos interativos.

---

<span id="integrações"></span>
## **Integrações**

<img src="https://raw.githubusercontent.com/Kauanrodrigues01/Kauanrodrigues01/refs/heads/main/images/evolution-api.png" width="180" alt="Evolution API" />

- Envio de mensagens automáticas pelo WhatsApp.
- Alertas de movimentações e baixo estoque.

<img src="https://raw.githubusercontent.com/Kauanrodrigues01/Kauanrodrigues01/refs/heads/main/images/gemini.png" width="150" alt="Gemini API" />

- IA para sugestões de reposição e insights de otimização.

---

<span id="visualizacao-do-sistema"></span>
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

<span id="como-configurar-o-projeto"></span>
## **🛠️ Como Configurar o Projeto**

<span id="executando-com-docker"></span>
### **Executando com Docker**

1. Vá ao site da [Google Ai studio](https://aistudio.google.com/apikey) e gere a sua chave de API gratuitamente.

2. Inicie os containers da evolution api:
```bash
docker compose -f docker-compose-evolution.yml up -d
```

3. Acesse a evolution na url: [http://localhost:8080/manager/](http://localhost:8080/manager/) e crie uma instância para o whatsApp e conecte-se através do QR code.

4. Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
```env
SECRET_KEY=django-insecure-h3y=dr4aic$ts$)z6_ngy%8!dkhd*n05l*wb1nwn+2ml&ep8qv
DEBUG=True 
ALLOWED_HOSTS=* 
LANGUAGE_CODE=pt-br 
TIME_ZONE=America/Fortaleza

# INTEGRATION WITH GEMINI API
GEMINI_API_KEY=api-key
GEMINI_MODEL=gemini-1.5-flash

# INTEGRATION WITH EVOLUTION API
MY_NUMBER=55*********
INSTANCE_NAME=test
INSTANCE_TOKEN=instance-token

# EMAIL
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=example@test.com
EMAIL_HOST_PASSWORD=@Test01020202010
MY_EMAIL=myemail@test.com

# Credentials for superuser
SUPERUSER_USERNAME=admin
SUPERUSER_EMAIL=admin@gmail.com
SUPERUSER_PASSWORD=admin
```

5. Construa e inicie os containers da aplicação:
```bash
docker build -t sge-app:0.0.1 .
docker compose -f docker-compose-dev.yml up -d
```

6. Agora os seguintes containers estarão rodando:
   - Aplicativo Django
   - PostgreSQL

7. Acesse o sistema em: [http://localhost:8000/](http://localhost:8000/)
