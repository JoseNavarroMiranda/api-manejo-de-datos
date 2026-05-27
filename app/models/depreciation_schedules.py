from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, DECIMAL, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class DepreciationSchedule(Base):
    __tablename__ = "depreciation_schedules"

    depreciation_id: Mapped[int] = mapped_column(
        "depreciation_id",
        primary_key=True,
        autoincrement=True,
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