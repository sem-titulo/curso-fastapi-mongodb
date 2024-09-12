import jwt

from fastapi import Depends, HTTPException, Request, status

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.settings import (
    SECRET_KEY_JWT,
)

token_auth_scheme = HTTPBearer()

# Função que valida se o token está presente e é válido
def validador_rota(credentials: HTTPAuthorizationCredentials = Depends(token_auth_scheme)):
    token = credentials.credentials  # Pega o token da requisição

    try:
        # Decodifica o token usando a SECRET_KEY
        decoded_token = jwt.decode(token, SECRET_KEY_JWT, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"error": "Token expirado, faça login novamente."}
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"error": "Token inválido."}
        )

    return decoded_token
