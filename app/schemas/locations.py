from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name : str
    address : str
    is_virtual: bool = False


class CategoryResponse(BaseModel):
    location_id: str
    name: str
    address : str
    is_virtual: bool