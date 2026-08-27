from app.schemas.locations import LocationCreate, MessageResponse, LocationUpdate
from app.models.locations import Location

from fastapi import HTTPException
from sqlalchemy.orm import Session


class LocationService:
    def __init__(self, db: Session):
        self.db = db


    def create_location(self, data: LocationCreate)-> Location:
        try: 
            location = Location (
                name=data.name,
                address=data.address,
                is_virtual=data.is_virtual
            )
            self.db.add(location)
            self.db.commit()
            self.db.refresh(location)
            return location
        except Exception as e:
            raise HTTPException(status_code=400, details=str(e))


    def update_location(self, location_id: str, data: LocationUpdate):
        location = self._get_Location_or_404(location_id)
        update_data = data.model_dump(exclude_unset=True)

        if not update_data:
            raise HTTPException(status_code=400, detail="No se enviaron datos en los campos, favor de validar")
        
        for fields, values in update_data.items():
            setattr(location, fields, values)

        try:
            self.db.commit()
            self.db.refresh(location)
        except Exception as e:
            raise HTTPException(status_code=500, details=str(e))
        return {"message": "Se actualizo de manera correcta"}


    def get_all_locations(self):
        location = self.db.query(Location).all()
        return location


    def _get_Location_or_404(self, location_id: str)->Location:
        """Funcion privada para que se pueda utilizar en otras funciones"""
        location = self.db.query(Location).filter(Location.location_id == location_id).first()
        if location is None:
            raise HTTPException(status_code=404, details="No se encuentrta una locacion al momento")
        return location
