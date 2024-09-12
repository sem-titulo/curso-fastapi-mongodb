from fastapi import APIRouter, Depends
from database.database import DBConnection
from utils.validador_rota import validador_rota

router = APIRouter(
    prefix="/notas",
    tags=["Notas"],
    dependencies=[Depends(validador_rota)]
)

db_connection = DBConnection()


@router.get('/')
def buscar_notas():
    notas = db_connection.find_one(
        "notas",
        {},
        {"_id": 0}
    )
    return {
        "messagem": notas
    }


@router.get('/exemplo')
def buscar_notas():
    print("Teste")
    return {
        "messagem": "Hello, world 3!"
    }
