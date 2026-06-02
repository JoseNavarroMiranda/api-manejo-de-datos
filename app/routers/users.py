from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.users import UserResponse, UserCreate
from app.service.users_service import UserService


router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.post(
        "/new_user",
        response_model=UserResponse,
        status_code=201        
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)