from datetime import date, datetime
from uuid import  uuid4

from sqlalchemy import CheckConstraint, Date, DateTime, DECIMAL, ForeignKey, Unicode, func, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Asset(Base):
    __tablename__ = "assets"

    __table_args__ = (
        CheckConstraint(
            "current_status IN ('Disponible', 'Asignado', 'Reparacion', 'Baja')",
            name="ck_assets_current_status",
        ),
    )

    asset_id: Mapped[int] = mapped_column(
        "asset_id",
        String(36),
        primary_key=True,
        autoincrement=False,
        default=lambda: str(uuid4())
    )

    asset_tag: Mapped[str] = mapped_column(
        "asset_tag",
        Unicode(20),
        nullable=False,
        unique=True,
    )

    serial_number: Mapped[str] = mapped_column(
        "serial_number",
        Unicode(100),
        nullable=False,
        unique=True,
        index=True,
    )

    model: Mapped[str] = mapped_column(
        "model",
        Unicode(100),
        nullable=False,
    )

    purchase_date: Mapped[date | None] = mapped_column(
        "purchase_date",
        Date,
        nullable=True,
    )

    purchase_cost: Mapped[float | None] = mapped_column(
        "purchase_cost",
        DECIMAL(18, 2),
        nullable=True,
    )

    current_status: Mapped[str] = mapped_column(
        "current_status",
        Unicode(20),
        nullable=False,
        default="Disponible",
    )

    category_id: Mapped[int] = mapped_column(
        "category_id",
        ForeignKey("categories.category_id"),
        nullable=False,
    )

    location_id: Mapped[int] = mapped_column(
        "location_id",
        ForeignKey("locations.location_id"),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        "created_at",
        DateTime(timezone=True),
        server_default=func.sysdatetimeoffset(),
        nullable=False,
    )