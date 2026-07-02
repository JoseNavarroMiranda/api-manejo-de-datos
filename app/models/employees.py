from uuid import uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Employee(Base):
    __tablename__ = "employees"

    employee_id: Mapped[str] = mapped_column(
        "employee_id",
        String(36),
        primary_key=True,
        autoincrement=False,
        default=lambda: str(uuid4())
    )

    name: Mapped[str] = mapped_column(
        "name",
        String(60),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        "last_name",
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        "email",
        String(100),
        nullable=False,
        unique=True,
        index=True,
    )

    departament: Mapped[str] = mapped_column(
        "departament",
        String(50),
        nullable=False,
    )

    cost_center: Mapped[str] = mapped_column(
        "cost_center",
        String(20),
        nullable=False,
    )