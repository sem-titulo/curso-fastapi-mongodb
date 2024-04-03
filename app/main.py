from fastapi import FastAPI

from app.routes import notas

app = FastAPI(
    title="Projeto bloco de notas",
    description="Exemplo de projeto FastAPI para a criação de bloco de notas"
)


app.include_router(notas.router)
