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






