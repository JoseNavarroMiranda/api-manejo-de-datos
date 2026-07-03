from datetime import datetime
from pydantic import BaseModel


class CategoryCrate(BaseModel):
    name : str 
    description : str | None = None


class CategoryResponse(BaseModel):
    category_id : str
    name : str
    description : str | None = None
    created_at: datetime