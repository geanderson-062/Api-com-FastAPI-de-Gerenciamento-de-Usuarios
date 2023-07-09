# para visualizar a api usar o comando uvicorn main:app --reload no cmd em seguida acessar a url fornecida pelo comd 
#ex: uvicorn main:app --reload

# primeiro passo importar o fast
from typing import Union
from fastapi import FastAPI

# segundo passo instanciar o fast api criando a variavel app 
app = FastAPI()

# terceiro passo usar um decorador para editar o caminho para envio dos dados 

# o decorador app.get na raiz diz para o fast.api que essa função de administrar os request que vão para raiz
@app.get("/")

# quarto passo definir a função , essa função vai ser chamada pelo fast toda vez que receber um request 
def read_root():

# quinto passo o que vai ser retornado para o usuário 
    return {"Hello": "World"}

# exemplo de uso do decorador

@app.get("/users")
def users_route():
    return {"Hello": "Users"}

# a url foi modificada no decorador para acessar ir na raiz /users 
# ex: http://127.0.0.1:8000/users