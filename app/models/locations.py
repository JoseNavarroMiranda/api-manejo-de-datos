from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Location(Base):
    __tablename__ = "locations"


    location_id: Mapped[int] = mapped_column(
        "location_id",
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        "name",
        String(100),
        nullable=False
    )

    address: Mapped[str] = mapped_column(
        "address",
        String(250),
        nullable=False,
    )

    is_virtual: Mapped[bool] = mapped_column(
        "is_virtual",
        Boolean,
        nullable=False,
        default=False,
    )