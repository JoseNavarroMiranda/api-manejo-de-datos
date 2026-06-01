from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/user",
    tags=["User"],
)

@router.post("/new_user")
def new_user():
    pass