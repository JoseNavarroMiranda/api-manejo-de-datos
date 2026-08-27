from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.categories import CategoryResponse, CategoryCreate, MessageResponse
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
    service_cat = CategoryService(db)
    return service_cat.create_category(category)


@router.put(
    "/update_cat/{category_id}",
    response_model=MessageResponse,
    status_code=201 
)
def update_category(category_id: str , category: CategoryCreate, db: Session = Depends(get_db)):
    service_cat = CategoryService(db)
    return service_cat.update_category(category_id, category)


@router.get(
    "/all_cat",
    response_model=list[CategoryResponse],
    status_code=200
)
def get_all_category(db: Session = Depends(get_db)):
    service_cat = CategoryService(db)
    return service_cat.get_all_category()


@router.get(
    "/cat/{category_id}",
    response_model=CategoryResponse,
    status_code=200
)
def get_cat_by_id(category_id: str, db: Session = Depends(get_db)):
    service_cat = CategoryService(db)
    return service_cat.get_cat_by_id(category_id)


@router.delete(
    "/dele_cat/{category_id}",
    response_model=MessageResponse,
    status_code=200
)
def delete_cat(category_id: str, db: Session = Depends(get_db)):
    service_cat = CategoryService(db)
    return service_cat.delete_cat(category_id)