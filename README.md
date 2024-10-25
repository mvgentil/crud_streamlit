
# Gerenciamento de Produtos

Este projeto é um sistema de gerenciamento de produtos desenvolvido com **FastAPI**, **SQLAlchemy** e **Pydantic** para o backend, e planejado para usar **Streamlit** no frontend. O gerenciamento de ambientes é feito com **Poetry** e **Pyenv**.

## Índice

- [Características](#características)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Endpoints da API](#endpoints-da-api)

## Características

- Cadastro de produtos com as seguintes informações:
  - Nome
  - Descrição
  - Preço
  - Categoria
  - Email do fornecedor
- Validação de categorias pré-definidas
- Geração automática de identificadores únicos para cada produto
- API RESTful para interagir com os dados

## Tecnologias Utilizadas

- **Backend:**
  - [FastAPI](https://fastapi.tiangolo.com/) - Um framework moderno e rápido para construção de APIs com Python.
  - [SQLAlchemy](https://www.sqlalchemy.org/) - Uma biblioteca SQL e ORM para Python.
  - [Pydantic](https://pydantic-docs.helpmanual.io/) - Para validação de dados e modelos.

- **Gerenciamento de Ambiente:**
  - [Poetry](https://python-poetry.org/) - Para gerenciar dependências e ambientes virtuais.
  - [Pyenv](https://github.com/pyenv/pyenv) - Para gerenciar múltiplas versões do Python.

- **Frontend (Futuro):**
  - [Streamlit](https://streamlit.io/) - Para construir aplicações web de maneira rápida e interativa.

## Instalação

### Pré-requisitos

1. Tenha o [Python](https://www.python.org/downloads/) instalado.
2. Instale o [Pyenv](https://github.com/pyenv/pyenv) para gerenciar as versões do Python.
3. Instale o [Poetry](https://python-poetry.org/docs/#installation) para gerenciar dependências.

### Passos para Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/mvgentil/crud_streamlit.git
   cd crud_streamlit/src/backend/
   ```

2. Instale as dependências:

   ```bash
   poetry install
   ```

3. Ative o ambiente virtual:

   ```bash
   poetry shell
   ```

4. Execute a aplicação:

   ```bash
   uvicorn src.backend.main:app --reload
   ```

   O Swagger da aplicação estará disponível em `https://127.0.0.1/docs`.

# API de Gerenciamento de Produtos

Esta API permite gerenciar produtos em um sistema, oferecendo funcionalidades para criar, ler, atualizar e deletar produtos.

## Endpoints da API

### 1. Criar um Produto

- **Método:** `POST`
- **URL:** `/products/`
- **Descrição:** Cria um novo produto no sistema.
- **Request Body:**
  - `name` (str): Nome do produto.
  - `description` (str): Descrição do produto.
  - `price` (float): Preço do produto.
  - `categoria` (str): Categoria do produto.
  - `email_fornecedor` (str): E-mail do fornecedor.
- **Response:**
  - **Código de Sucesso:** 200 Created
  - **Corpo:** Retorna o produto criado com os detalhes.
  
### 2. Obter Todos os Produtos

- **Método:** `GET`
- **URL:** `/products/`
- **Descrição:** Retorna uma lista de todos os produtos no sistema.
- **Response:**
  - **Código de Sucesso:** 200 OK
  - **Corpo:** Retorna uma lista de produtos.

### 3. Obter um Produto por ID

- **Método:** `GET`
- **URL:** `/products/{product_id}`
- **Descrição:** Retorna os detalhes de um produto específico pelo seu ID.
- **Path Parameters:**
  - `product_id` (int): ID do produto.
- **Response:**
  - **Código de Sucesso:** 200 OK
  - **Corpo:** Retorna o produto correspondente.
  - **Código de Erro:** 404 Product Not Found (se o produto não for encontrado)

### 4. Atualizar um Produto

- **Método:** `PUT`
- **URL:** `/products/{product_id}`
- **Descrição:** Atualiza os detalhes de um produto específico pelo seu ID.
- **Path Parameters:**
  - `product_id` (int): ID do produto.
- **Request Body:**
  - `name` (str, opcional): Nome do produto.
  - `description` (str, opcional): Descrição do produto.
  - `price` (float, opcional): Preço do produto.
  - `categoria` (str, opcional): Categoria do produto.
  - `email_fornecedor` (str, opcional): E-mail do fornecedor.
- **Response:**
  - **Código de Sucesso:** 200 OK
  - **Corpo:** Retorna o produto atualizado.
  - **Código de Erro:** 404 Product Not Found (se o produto não for encontrado)

### 5. Deletar um Produto

- **Método:** `DELETE`
- **URL:** `/products/{product_id}`
- **Descrição:** Remove um produto específico pelo seu ID.
- **Path Parameters:**
  - `product_id` (int): ID do produto.
- **Response:**
  - **Código de Sucesso:** 200 OK
  - **Corpo:** Retorna o produto deletado.
  - **Código de Erro:** 404 Product Not Found (se o produto não for encontrado)

### TODO

- Frontend com Streamlit