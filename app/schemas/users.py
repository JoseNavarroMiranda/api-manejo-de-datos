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
    password: str
    role: str
    created_at: datetime
    updated_at: datetime | None





