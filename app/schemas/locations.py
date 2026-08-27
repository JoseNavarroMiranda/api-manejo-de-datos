from pydantic import BaseModel


class LocationCreate(BaseModel):
    name : str
    address : str
    is_virtual: bool = False


class LocationResponse(BaseModel):
    location_id: str
    name: str
    address : str
    is_virtual: bool


class LocationUpdate(BaseModel):
    name: str | None = None
    address : str | None = None
    is_virtual: bool | None = None


class MessageResponse(BaseModel):
    message: str