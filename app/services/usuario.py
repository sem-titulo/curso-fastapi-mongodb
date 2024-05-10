import base64
from datetime import datetime
from uuid import uuid4
from database.database import DBConnection


class UsuarioService:
    def __init__(self):
        self.db_connection = DBConnection()
        return

    def criar_usuario(self, data):
        data["id"] = str(uuid4())
        data["criado_em"] = datetime.now().isoformat()
        data["senha"] = base64.b64encode(bytes(data["senha"], "utf-8"))
        self.db_connection.insert_one("usuarios", data)
        return data

    def listar_usuarios(self, email):
        query = {}
        if email:
            query["email"] = email
        return self.db_connection.find("usuarios", query, {"_id": 0, "senha": 0})

    def listar_usuario(self, id):
        return self.db_connection.find_one("usuarios", {"id": id}, {"_id": 0, "senha": 0})
