from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


# Criando uma instância da aplicação FastAPI
app = FastAPI()

# Configuração do banco de dados
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost/flask_react_crud"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definição do modelo de usuário
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100))
    data = Column(DateTime, default=datetime.now)

# Classe de modelo para receber dados do usuário
class UsuarioCreate(BaseModel):
    nome: str
    email: str

# Classe de modelo para retornar dados do usuário
class UsuarioOut(BaseModel):
    id: int
    nome: str
    email: str
    data: datetime

# Rota inicial para teste
@app.get("/")
def hello_world():
    return {"message": "Olá, Mundo!"}

# Rota para listar todos os usuários
@app.get("/listadeusuarios")
def listadeusuarios():
    db = SessionLocal()
    usuarios = db.query(Usuario).all()
    return usuarios

# Rota para obter os detalhes de um usuário específico
@app.get("/detalhedousuario/{id}")
def detalhedousuario(id: int):
    db = SessionLocal()
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

# Rota para atualizar um usuário
@app.put("/atualizarusuario/{id}")
def atualizarusuario(id: int, usuario: UsuarioCreate):
    db = SessionLocal()
    usuario_db = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuario_db.nome = usuario.nome
    usuario_db.email = usuario.email
    db.commit()
    db.refresh(usuario_db)
    return usuario_db

# Rota para deletar um usuário
@app.delete("/deletarusuario/{id}")
def deletarusuario(id: int):
    db = SessionLocal()
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(usuario)
    db.commit()
    return {"message": "Usuário deletado com sucesso"}

# Rota para adicionar um novo usuário
@app.post("/usuarioadd")
def usuarioadd(usuario: UsuarioCreate):
    db = SessionLocal()
    novo_usuario = Usuario(nome=usuario.nome, email=usuario.email)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

# Execução da aplicação FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
