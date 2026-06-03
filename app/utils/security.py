from pwdlib import PasswordHash

_password_hash = PasswordHash.recommended()

def hash_password(password: str)->str:
    """Funcion que recibe el pass en texto plano de metodo post y realizar el encryptado"""
    return _password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str)->bool:
    """Funcion que hacer validacion sobre password en texto plano 
        y password con hash, devulve un valor true o false"""
    return _password_hash.verify(plain_password, hashed_password)

