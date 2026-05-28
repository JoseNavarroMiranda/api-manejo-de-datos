from datetime import datetime

from sqlalchemy import String, Unicode, DateTime, func, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint(
            "role IN ('viewer', 'editor', 'admin')",
            name="ck_users_role",
        ),
    )

    user_id: Mapped[int] = mapped_column(
        "user_id",
        primary_key=True,
        autoincrement=True,
    )

    username: Mapped[str] = mapped_column(
        "username",
        String(30),
        nullable=False,
        unique=True,
    )

    password: Mapped[str] = mapped_column(
        "password",
        String(18),
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        "role",
        Unicode(20),
        nullable=False,
        default="viewer",
    )
    created_at: Mapped[datetime] = mapped_column(
        "created_at",
        DateTime(timezone=True),
        server_default=func.sysdatetimeoffset(),
        nullable=False,
    )