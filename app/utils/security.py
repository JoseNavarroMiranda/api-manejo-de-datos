from pwdlib import PasswordHash
from datetime import datetime, timezone, timedelta
import jwt
import os

_password_hash = PasswordHash.recommended()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30))



def hash_password(password: str)->str:
    """Funcion que recibe el pass en texto plano de metodo post y realizar el encryptado"""
    return _password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str)->bool:
    """Funcion que hacer validacion sobre password en texto plano 
        y password con hash, devulve un valor true o false"""
    return _password_hash.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt