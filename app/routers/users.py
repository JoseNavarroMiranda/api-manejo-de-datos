from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.users import UserResponse, UserCreate, UserUpdate, MessageResponse
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


@router.get(
        "/allusers",
        response_model=list[UserResponse],
        status_code=200
)
def get_all_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()


@router.get(
        "/{user_id}",
        response_model=UserResponse,
        status_code=200
)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_user_by_id(user_id)


@router.put(
        "/user_pass_update/{user_id}",
        response_model=MessageResponse,
        status_code=200 
)
def update_password_user(user: UserUpdate, user_id, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.update_password_user(user_id, user)


@router.put(
        "/disable_user/{user_id}",
        reponse_model=MessageResponse,
        status_code=200
)
def disable_user(user: UserUpdate, user_id, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.disable_user(user_id, user)