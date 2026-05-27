from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Integer, Unicode, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    audit_id: Mapped[int] = mapped_column(
        "audit_id",
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    table_name: Mapped[str] = mapped_column(
        "table_name",
        Unicode(50),
        nullable=False,
    )

    record_id: Mapped[int] = mapped_column(
        "record_id",
        Integer,
        nullable=False,
    )

    action: Mapped[str] = mapped_column(
        "action",
        Unicode(10),
        nullable=False,
    )

    old_value: Mapped[str | None] = mapped_column(
        "old_value",
        Unicode,
        nullable=True,
    )

    new_value: Mapped[str | None] = mapped_column(
        "new_value",
        Unicode,
        nullable=True,
    )

    changed_by: Mapped[str] = mapped_column(
        "changed_by",
        Unicode(100),
        nullable=False,
    )

    changed_at: Mapped[datetime] = mapped_column(
        "changed_at",
        DateTime(timezone=True),
        server_default=func.sysdatetimeoffset(),
        nullable=False,
    )