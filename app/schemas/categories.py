from datetime import datetime
from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name : str 
    description : str | None = None


class CategoryResponse(BaseModel):
    category_id : str
    name : str
    description : str | None = None
    created_at: datetime


class CategoryUpdate(BaseModel):
    name: str | None  = None
    description: str | None = None



class MessageResponse(BaseModel):
    message: str