from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.locations import LocationResponse, LocationCreate, MessageResponse, LocationUpdate
from app.service.locations.location_service import LocationService

router = APIRouter (
    prefix="/location",
    tags=["location"],
)

@router.post(
    "/create_loc",
    response_model=LocationResponse,
    status_code=201,
)
def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    service_loc = LocationService(db)
    return service_loc.create_location(location)


@router.get(
    "/all_loc",
    response_model=list[LocationResponse],
    status_code=200,
)
def get_all_locations(db: Session = Depends(get_db)):
    service_loc = LocationService(db)
    return service_loc.get_all_locations()


@router.put(
    "/update_loc/{location_id}",
    response_model=MessageResponse,
    status_code=201
)
def update_location(location_id: str, location: LocationUpdate, db: Session = Depends(get_db)):
    service_loc = LocationService(db)
    return service_loc.update_location(location_id, location)


@router.get(
    "/loc/{location_id}",
    response_model=LocationResponse,
    status_code=200
)
def get_loc_by_id(location_id: str, db: Session = Depends(get_db)):
    service_loc = LocationService(db)
    return service_loc._get_Location_or_404(location_id)