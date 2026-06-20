from datetime import datetime

from sqlalchemy import String, Unicode, DateTime, func, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from uuid import  uuid4


from app.database import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint(
            "role IN ('viewer', 'editor', 'admin')",
            name="ck_users_role",
        ),
    )

    user_id: Mapped[str] = mapped_column(
        "user_id",
        String(36),
        primary_key=True,
        autoincrement=False,
        default=lambda: str(uuid4())
    )

    username: Mapped[str] = mapped_column(
        "username",
        String(30),
        nullable=False,
        unique=True,
    )

    password: Mapped[str] = mapped_column(
        "password",
        String(255),
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        "role",
        Unicode(25),
        nullable=False,
        default="viewer",
    )

    status: Mapped[bool] = mapped_column(
        "status",
        nullable=False,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        "created_at",
        DateTime(timezone=True),
        server_default=func.sysdatetimeoffset(),
        nullable=False,
    )
    
    updated_at: Mapped[datetime | None] = mapped_column(
        "updated_at",
        DateTime(timezone=True),
        nullable=True,
    )