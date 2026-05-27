from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Unicode, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Assignment(Base):
    __tablename__ = "assignments"

    assignment_id: Mapped[int] = mapped_column(
        "assignment_id",
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    asset_id: Mapped[int] = mapped_column(
        "asset_id",
        ForeignKey("assets.asset_id"),
        nullable=False,
    )

    employee_id: Mapped[int] = mapped_column(
        "employee_id",
        ForeignKey("employees.employee_id"),
        nullable=False,
    )

    assignment_date: Mapped[datetime] = mapped_column(
        "assignment_date",
        DateTime(timezone=True),
        server_default=func.sysdatetimeoffset(),
        nullable=False,
    )

    return_date: Mapped[datetime | None] = mapped_column(
        "return_date",
        DateTime(timezone=True),
        nullable=True,
    )

    condition_on_return: Mapped[str | None] = mapped_column(
        "condition_on_return",
        Unicode(255),
        nullable=True,
    )