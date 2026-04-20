from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel

if TYPE_CHECKING:
    from .User import User


class RefreshToken(BaseModel):
    __tablename__ = "refresh_token"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    token_hash: Mapped[str] = mapped_column(
        String(60),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )
    revoked_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True
    )

    user: Mapped["User"] = relationship(back_populates="refresh_tokens")
