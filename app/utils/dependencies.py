import jwt
import os
from fastapi import Header, HTTPException

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')


def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="No se encuentra autorizado")
    token = authorization

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detal="Sesion expirada")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Operacion Invalida")