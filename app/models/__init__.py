from app.models.assets import Asset
from app.models.audit_logs import AuditLog
from app.models.categories import Category
from app.models.depreciation_schedules import DepreciationSchedule
from app.models.employees import Employee
from app.models.locations import Location
from app.models.maintenance_logs import MaintenanceLog
from app.models.assignaments import Assignment


__all__ = [
    "Asset",
    "Assignment",
    "Category",
    "DepreciationSchedule",
    "Employee",
    "Location",
    "MaintenanceLog",
    "AuditLog",
]