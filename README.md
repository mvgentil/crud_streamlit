
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
   cd crud_streamlit
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
   uvicorn main:app --reload
   ```

   O Swagger da aplicação estará disponível em `https://127.0.0.1/docs`.

## Endpoints da API

### POST /products/

Cria um novo produto.

**Body:**
```json
{
  "name": "Nome do produto",
  "description": "Descrição do produto",
  "price": 99.99,
  "categoria": "Eletrônicos",
  "email_fornecedor": "fornecedor@example.com"
}
```

**Resposta:**
- Status: 201 Created
- Body:
```json
{
  "id": 1,
  "name": "Nome do produto",
  "description": "Descrição do produto",
  "price": 99.99,
  "categoria": "Eletrônicos",
  "email_fornecedor": "fornecedor@example.com",
  "created_at": "2024-10-25T00:00:00Z"
}
```

### TODO

- getProduct, getProducts, deleteProduct, updateProduct
- Frontend com Streamlit