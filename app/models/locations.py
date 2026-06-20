
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4


from app.database import Base

class Location(Base):
    __tablename__ = "locations"


    location_id: Mapped[str] = mapped_column(
        "location_id",
        String(36),
        primary_key=True,
        autoincrement=False,
        default=lambda: str(uuid4())
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