from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel

if TYPE_CHECKING:
    from .Client import Client


class RedirectURI(BaseModel):
    __tablename__ = "redirect_uri"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))
    redirect_uri: Mapped[str] = mapped_column(
        String(128),
        nullable=False
    )

    client: Mapped["Client"] = relationship(back_populates="redirect_uris")
