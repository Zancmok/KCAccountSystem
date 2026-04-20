from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel

if TYPE_CHECKING:
    from .User import User
    from .RedirectURI import RedirectURI


class Client(BaseModel):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    client_id: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=True
    )
    client_secret: Mapped[str] = mapped_column(
        String(60),
        nullable=False
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
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )

    user: Mapped["User"] = relationship(back_populates="clients")
    redirect_uris: Mapped[list["RedirectURI"]] = relationship(
        back_populates="client",
        cascade="all, delete-orphan"
    )
