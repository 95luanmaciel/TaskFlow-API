from fastapi import FastAPI

#importa o motor e a classe Base do database.py
from database import engine, Base

#sqlalchemy analisa todos os modelos que herdam de "Base" e os cria se não existirem no postgresql
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Minha API de tarefas")
@app.get("/")
def rodando():
    return{"mensage": "Fast API e Uvicorn funcionando com sucesso"} 