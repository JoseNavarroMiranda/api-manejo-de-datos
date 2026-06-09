from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas.users import LoginRequest, TokenResponse
from app.utils.security import verify_password, create_access_token


class LoginService:
    def __init__(self, db: Session):
        self.db = db

    def _get_username_or_404(self, username : str):
        user = self.db.query(User).filter(User.username == username).first()
        if user is None:
            raise HTTPException(status_code=401, detail="Error al iniciar sesion")
        if not user.status:
            raise HTTPException(status_code=403, detail="La cuenta se encuentra deshabilidtada")
        return user  
    

    def login_user(self, data: LoginRequest):
        user = self._get_username_or_404(data.username)
        if not verify_password(data.password, user.password):
            raise HTTPException(status_code=401, detail="Usuario o passsword incorrecto")
        token = create_access_token({"sub": data.username, "role": user.role})
        return TokenResponse(access_token=token, token_type="bearer", message="Inicio de sesion correcto")
        
