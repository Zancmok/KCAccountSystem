from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel

if TYPE_CHECKING:
    from .RefreshToken import RefreshToken


class User(BaseModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        unique=True
    )
    password_hash: Mapped[str] = mapped_column(
        String(60),
        nullable=False
    )
    profile_picture_url: Mapped[str] = mapped_column(
        String(128),
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )
    last_login: Mapped[datetime] = mapped_column(DateTime)

    refresh_tokens: Mapped[list["RefreshToken"]] = relationship(back_populates="user")
