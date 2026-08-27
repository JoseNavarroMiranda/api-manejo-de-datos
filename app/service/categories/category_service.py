from app.models.categories import Category
from app.schemas.categories import CategoryCreate, CategoryUpdate

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


    def update_category(self, category_id: str, data: CategoryUpdate):
        """Funcion que realiza actualizacion de category, primero se realiza validacion en los campos de update
            utilizando la funcion de model_dump, se realiza la iteracion del data para hacer update y posteriormente
            en el bloque de try recibe si hay algun error al guardar en la db"""
        category = self._get_category_or_404(category_id)
        update_data = data.model_dump(exclude_unset=True)

        if not update_data:
            raise HTTPException(status_code=400, detail="No se enviaron campos para actualizar")
        
        for field, value in update_data.items():
            setattr(category, field, value)
            
        try:
            self.db.commit()
            self.db.refresh(category)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
                        
        return {"message": "Se actualizo la categoria de manera correcta"}


    def delete_cat(self, category_id: str):
        category = self._get_category_or_404(category_id)
        
        try:
            self.db.delete(category)
            self.db.commit()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        return {"message" : "Se elimino la categoria de manera correcta"}

    def get_all_category(self):
        categories = self.db.query(Category).all()
        return categories


    def get_cat_by_id(self, category_id):
        category = self.db.query(Category).filter(Category.category_id == category_id).first()
        if category is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return category


    def _get_category_or_404(self, category_id: str)-> Category:
        """Funcino que permite realizar la busqueda por id"""
        category = self.db.query(Category).filter(Category.category_id == category_id).first()
        if category is None:
            raise HTTPException(status_code=404, details="Categoria no encontrada")
        return category

    
    def _get_category_by_name(self, name: str)-> None:
        """Funcion privada que permitira realizar busqueda de otras funciones"""
        category_exists = self.db.query(Category).filter(Category.name == name).first()
        if category_exists:
            raise HTTPException(status_code=400, details="El nombre de la categoria, no existe")


