from datetime import datetime
from pydantic import BaseModel

class AssignamentCreate(BaseModel):
    asset_id: int
    employee_id: int
    assignament_date: datetime | None = None


class AssignamentRead(AssignamentCreate):
    assignament_id: int
    return_date: datetime | None = None