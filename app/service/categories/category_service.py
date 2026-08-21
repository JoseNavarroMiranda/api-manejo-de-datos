from app.models.categories import Category
from app.schemas.categories import CategoryCreate

from fastapi import HTTPException
from sqlalchemy.orm import Session

class CategoryService:
    def __init__(self, db: Session):
        self.db = db


    def create_category(self, data: CategoryCreate)-> Category:
        """Funcion que permite crear una nueva categoria"""
        try:
            category = Category (
                name=data.name,
                description=data.description,
            )
            self.db.add(category )
            self.db.commit()
            self.db.refresh(category)
            return category
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))



    def update_category():
        pass


    def delete_category():
        pass


    def get_all_category():
        pass


    def get_category_by_name():
        pass


