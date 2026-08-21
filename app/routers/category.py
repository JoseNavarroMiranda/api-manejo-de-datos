from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.categories import CategoryResponse, CategoryCreate
from app.service.categories.category_service import CategoryService

router = APIRouter(
    prefix="/category",
    tags=["category"],
)

@router.post(
    "/create_cat",
    response_model=CategoryResponse,
    status_code=201
)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    category = CategoryService(db)
    return category.create_category(category)