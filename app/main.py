from fastapi import FastAPI


app = FastAPI(
    title="Projeto bloco de notas",
    description="Exemplo de projeto FastAPI para a criação de bloco de notas"
)


@app.get('/exemplo')
def buscar_notas():
    print("Teste")
    return {
        "messagem": "Hello, world 3!"
    }