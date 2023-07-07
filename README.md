# Introdução

Este é um sistema que utiliza o framework FastAPI para criar uma API. Para visualizar a API, siga as instruções abaixo:

# Passo 1:

Certifique-se de ter o pacote Uvicorn instalado. Caso contrário, instale-o usando o comando:

pip install uvicorn

# Passo 2:

No prompt de comando, execute o seguinte comando para iniciar o servidor:


uvicorn main:app --reload

# Passo 3:
Acesse a URL fornecida pelo comando anterior no navegador. Por exemplo:


http://localhost:8000
A página inicial exibirá a mensagem "Hello, World". Você também pode acessar a rota "/users" para obter a mensagem "Hello, Users".

Cada rota é definida por meio de um decorador @app.get seguido pelo caminho desejado. As funções decoradas com esses caminhos serão executadas quando uma solicitação for feita para o respectivo caminho.

Este é apenas um exemplo básico de uso do FastAPI para criar uma API. .
 
