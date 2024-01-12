# Api com FastAPI de Gerenciamento de Usuários

## Descrição

Esta é uma aplicação backend desenvolvida com FastAPI, uma framework moderna e de alta performance para a construção de APIs com Python. A aplicação fornece uma série de endpoints RESTful para o gerenciamento de usuários, incluindo a criação, leitura, atualização e exclusão de registros de usuários (CRUD). Ela utiliza o SQLAlchemy para interações com o banco de dados MySQL e é estruturada em torno de operações básicas relacionadas a usuários.

## Funcionalidades

- **Criação de Usuários**: Adicione novos usuários ao banco de dados.
- **Listagem de Usuários**: Obtenha uma lista de todos os usuários cadastrados.
- **Detalhes do Usuário**: Acesse os detalhes de um usuário específico.
- **Atualização de Usuários**: Atualize as informações de um usuário existente.
- **Exclusão de Usuários**: Remova um usuário do banco de dados.

## Instalação

Para rodar esta aplicação, você precisará do Python instalado em sua máquina, além dos seguintes pacotes:

- FastAPI
- Uvicorn (para servir a aplicação)
- SQLAlchemy
- PyMySQL (ou outro conector compatível com o banco de dados MySQL)
- Pydantic

Você pode instalar todas as dependências necessárias com o seguinte comando:

```bash
pip install fastapi uvicorn sqlalchemy pymysql pydantic
```

## Configuração do Banco de Dados

Antes de executar a aplicação, certifique-se de ter o MySQL rodando em sua máquina e de criar um banco de dados chamado `flask_react_crud`. Você também pode alterar a string de conexão do banco de dados no arquivo da aplicação para corresponder à sua configuração local.

## Execução da Aplicação

Para iniciar a aplicação, execute o seguinte comando na raiz do diretório:

```bash
uvicorn main:app --reload
```

A aplicação estará disponível em `http://localhost:8000`.

## Endpoints da API

- `GET /`: Retorna uma mensagem de boas-vindas.
- `POST /usuarioadd`: Adiciona um novo usuário.
- `GET /listadeusuarios`: Lista todos os usuários.
- `GET /detalhedousuario/{id}`: Mostra os detalhes de um usuário específico.
- `PUT /atualizarusuario/{id}`: Atualiza um usuário existente.
- `DELETE /deletarusuario/{id}`: Deleta um usuário.

## Contribuição

Contribuições para a melhoria da aplicação são sempre bem-vindas. Sinta-se livre para clonar o repositório e enviar seus pull requests.

---

Este README fornece um guia básico para a instalação, configuração e uso da aplicação. Para mais informações, consulte a documentação oficial do FastAPI e do SQLAlchemy.
