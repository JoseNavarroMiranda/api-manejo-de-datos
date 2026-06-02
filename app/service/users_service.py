from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas.users import UserCreate

#Modulo para creacion de usuario,tratar de dejar comentarios de creacion en las funciones utilizando tripe comilla

class UserService:
    def __init__(self, db: Session):
        """Funcion done se realiza la validacion de tabla
            se utiliza session para poder validar los campos de la tabla Users"""
        self.db = db
    def create_user(self, data: UserCreate) -> User:
        user = User(
            username=data.username,
            password=data.password,
            role=data.role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
