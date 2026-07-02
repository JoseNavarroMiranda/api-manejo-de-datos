from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.users import LoginRequest, TokenResponse
from app.service.login.login_service import LoginService

router = APIRouter(
    prefix="/login",
    tags=["login"]
)

@router.post(
    "/login_user",
    response_model=TokenResponse,
    status_code=200
)
def login_user(user: LoginRequest, db: Session = Depends(get_db)):
    service = LoginService(db)
    return service.login_user(user)
