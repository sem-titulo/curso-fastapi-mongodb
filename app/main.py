from fastapi import FastAPI

from app.routes import notas, usuario, authenticate

app = FastAPI(
    title="Projeto bloco de notas",
    description="Exemplo de projeto FastAPI para a criação de bloco de notas"
)


app.include_router(usuario.router)
app.include_router(authenticate.router)
app.include_router(notas.router)
