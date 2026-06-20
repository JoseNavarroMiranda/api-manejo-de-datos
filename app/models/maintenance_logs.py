from datetime import datetime
from decimal import Decimal

from sqlalchemy import  DateTime, DECIMAL, ForeignKey, Unicode, func, String
from sqlalchemy.orm import Mapped, mapped_column
from uuid import  uuid4

from app.database import Base


class MaintenanceLog(Base):
    __tablename__ = "maintenance_logs"

    log_id: Mapped[str] = mapped_column(
        "log_id",
        String(36),
        primary_key=True,
        autoincrement=False,
        default=lambda: str(uuid4())
    )

    asset_id: Mapped[int] = mapped_column(
        "asset_id",
        ForeignKey("assets.asset_id"),
        nullable=False,
    )

    maintenance_date: Mapped[datetime] = mapped_column(
        "maintenance_date",
        DateTime(timezone=True),
        server_default=func.sysdatetimeoffset(),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        "description",
        Unicode,
        nullable=False,
    )

    technician_name: Mapped[str] = mapped_column(
        "technician_name",
        Unicode(100),
        nullable=False,
    )

    cost: Mapped[Decimal] = mapped_column(
        "cost",
        DECIMAL(18, 2),
        nullable=False,
    )