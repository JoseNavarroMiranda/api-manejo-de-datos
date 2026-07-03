from app.models.categories import Category
from app.schemas.categories import CategoryCrate

from fastapi import HttpEce
from sqlalchemy.orm import Session

class CategoryService:
    def __init__(self, db: Session):
        self.db = db


    def create_category():
        pass

