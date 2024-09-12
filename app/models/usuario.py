import re
from pydantic import BaseModel, EmailStr, constr, validator, Field

class UsuarioModel(BaseModel):
    email: EmailStr
    senha: constr(min_length=8)

    @validator("senha")
    def validator_senha(cls, v):
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()-_+]).+$", v):
            raise ValueError("A senha deve conter pelo menos uma letra minúscula, uma letra maiúscula, um número e um caractere especial")
        return v

class EditarUsuarioModel(BaseModel):
    email: EmailStr


class LoginModel(BaseModel):
    email: str
    senha: str
