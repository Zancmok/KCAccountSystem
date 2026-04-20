from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel

if TYPE_CHECKING:
    from .Client import Client


class RedirectURI(BaseModel):
    __tablename__ = "redirect_uri"

    id: Mapped[int] = mapped_column(primary_key=True)
