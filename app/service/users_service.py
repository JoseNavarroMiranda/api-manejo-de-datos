from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas.users import UserCreate
from app.utils.security import hash_password

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, data: UserCreate) -> User:
        """Crea un nuevo usuario adicional que se realice el hash de la pass"""
        user = User(
            username=data.username,
            password=hash_password(data.password),
            role=data.role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_all_users(self):
        users = self.db.query(User).all()
        return users
    

