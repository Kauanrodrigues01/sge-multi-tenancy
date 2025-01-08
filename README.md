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
  - Envio de mensagens automáticas via WhatsApp (API da **Envolution**).
  - Envio de e-mails com o próprio Django.

---

## **Tecnologias Utilizadas**
- **Back-end**:
  - **Django** para o criação do sistema web e gerenciamento do sistema e envio de e-mails.
  - Integração com a API da Envolution para envio de mensagens WhatsApp.
  - **Gemini** para integração de IA e fornecimento de insights.
- **Front-end**:
  - **Bootstrap** para estilização.
  - **Chart.js** para criação de gráficos interativos.

---

## **Visualização do Sistema**

### **Gráficos**

- **Valor de Vendas (últimos 7 dias):**
- **Quantidade de Vendas Diárias (últimos 7 dias):**
- **Produtos por Marca:**
- **Produtos por Categoria:**

> *Adicione aqui imagens de exemplos de gráficos gerados.*

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

> *Adicione aqui imagens de exemplos de visualização de métricas.*

---

## **Integrações**

### **Envolution**
![Logo Envolution](#) *(Adicione a logo pequena aqui)*

- Envio de mensagens automáticas pelo WhatsApp.
- Alertas de movimentações e baixo estoque.

### **Gemini**
![Logo Gemini](#) *(Adicione a logo pequena aqui)*

- IA para sugestões de reposição e insights de otimização.

---

## **Como Configurar o Projeto**

### **Pré-requisitos**
1. Python 3.10+
2. Django 4.2+
3. Node.js (para dependências do Chart.js, se aplicável)
4. Conta na API da Envolution
5. Configuração do Gemini para integração de IA

### **Instalação**
```bash
# Clone o repositório
$ git clone https://github.com/seuprojeto/sge.git

# Acesse a pasta do projeto
$ cd sge

# Instale as dependências Python
$ pip install -r requirements.txt

# Realize as migrações
$ python manage.py migrate

# Inicie o servidor
$ python manage.py runserver
```

---

## **Contribuição**
Contribuições são bem-vindas! Por favor, siga as diretrizes do projeto ao enviar pull requests.

---

## **Licença**
Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

## **Contato**
Caso tenha dúvidas ou sugestões, entre em contato:
- **Email:** exemplo@dominio.com
- **WhatsApp:** +55 11 99999-9999

