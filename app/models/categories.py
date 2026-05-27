from datetime import datetime, timezone 

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    category_id: Mapped[int] = mapped_column(
        "category_id",
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        "name",
        String(70),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        "description",
        String(200),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        "created_at",
        DateTime(timezone=True),
        server_default=func.sysdatetimeoffset(),
        nullable=False,
    )