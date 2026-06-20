from app.models.users import User
from app.schemas.users import UserCreate, UserUpdate
from app.utils.security import hash_password
from datetime import datetime, timezone


from fastapi import HTTPException
from sqlalchemy.orm import Session

class UserService:
    def __init__(self, db: Session):
        self.db = db


    def create_user(self, data: UserCreate) -> User:
        """Crea un nuevo usuario adicional que se realice el hash de la pass utiliza dos funciones de busqueda de usuario y funcion de rol"""
        self._valid_roles(data.role)
        self._valid_user_exist(data.username)
        try:
            user = User(
                username=data.username,
                password=hash_password(data.password),
                role=data.role,
            )
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    def get_all_users(self):
        users = self.db.query(User).all()
        return users


    def get_user_by_id(self,user_id):
        user = self.db.query(User).filter(User.user_id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user


    def update_password_user(self, user_id, data: UserUpdate):
        user = self._get_user_or_404(user_id)
        try:
            user.password = hash_password(data.password)
            user.updated_at = datetime.now(timezone.utc)
            self.db.commit()
            self.db.refresh(user)
            return {"message": "Contraseña actualizada correctamente"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    def update_role_user(self, user_id, data: UserUpdate):
        user = self._get_user_or_404(user_id)
        self._valid_roles(data.role)
        try:
            user.role = data.role
            user.updated_at = datetime.now(timezone.utc)
            self.db.commit()
            self.db.refresh(user)
            return { "message" : "El rol de usuario fue actualizado correctamente"}
        except Exception as e:
            raise HTTPException(status_code = 400, detail=str(e))


    def disable_user(self, user_id, data: UserUpdate):
        """Funcion para realizar operacion de desabilitar o habilitar usuario
            realiza validacion si el body de status no es None, para evitar que se cambiar valor bool"""
        user = self._get_user_or_404(user_id)
        try:
            if data.status is not None:
                user.status = data.status
            user.updated_at = datetime.now(timezone.utc)
            self.db.commit()
            self.db.refresh(user)
            mensaje = "Usuario habilitado correctamente" if user.status else "Usuario deshabilitado correctamente"
            return {"message": mensaje}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    def _get_user_or_404(self, user_id: str) -> User:
        """Funcion que se utiliza para la busqueda de usuario en otras funciones de update, esto para evitar DRY"""
        user = self.db.query(User).filter(User.user_id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user


    def _valid_roles(self, role: str)-> None:
        valid_roles =  {"viewer", "editor", "admin"}
        if role not in valid_roles:
            raise HTTPException(
                status_code = 400,
                detail=f"Rol no valido: debe de ser {', '.join(valid_roles)}"
            )


    def _valid_user_exist(self, username: str)-> None:
        user_exists = self.db.query(User).filter(User.username == username).first()
        if user_exists:
            raise HTTPException(status_code=400, detail="Este username ya esta en uso")
        
