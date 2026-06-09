from pydantic import BaseModel 
#Pydantic permite hacer la validaciones de que es lo se recibira y da respuesta
from datetime import datetime


class UserCreate(BaseModel):
    """Clase donde se colocan los campos y el tipo de dato que este debe de recibit"""
    username: str
    password: str
    role: str


class UserResponse(BaseModel):
    """Clase donde se colocan los datos que se mandaran a llamar con peticiones post"""
    user_id: int
    username: str
    role: str
    status: bool
    created_at: datetime
    updated_at: datetime | None


class UserUpdate(BaseModel):
    """Clase que utilizara el metodo put para realizar actualizacion de password"""
    username: str | None = None
    password: str | None = None
    status: bool | None = None
    role: str | None = None


class MessageResponse(BaseModel):
    """Clase que se utilizara para poder pasar el comentario de la peticion"""
    message: str


class LoginRequest(BaseModel):
    """Clase que recibe dos parametros y permite realizar el login de usuario"""
    username: str
    password: str


class TokenResponse(BaseModel):
    """Clase que reponse el token para la creacion de este mismo"""
    access_token: str
    token_type: str 
    message: str





