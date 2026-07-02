from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, DECIMAL, ForeignKey, Integer, func, String
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4

from app.database import Base


class DepreciationSchedule(Base):
    __tablename__ = "depreciation_schedules"

    depreciation_id: Mapped[str] = mapped_column(
        "depreciation_id",
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

    fiscal_year: Mapped[int] = mapped_column(
        "fiscal_year",
        Integer,
        nullable=False,
    )

    depreciated_value: Mapped[Decimal] = mapped_column(
        "depreciated_value",
        DECIMAL(18, 2),
        nullable=False,
    )

    calculation_date: Mapped[datetime] = mapped_column(
        "calculation_date",
        DateTime(timezone=True),
        server_default=func.sysdatetimeoffset(),
        nullable=False,
    )