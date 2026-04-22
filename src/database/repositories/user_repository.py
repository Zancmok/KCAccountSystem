from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database.models import User
from database.database import sql_engine
from errors import UserAlreadyExistsError
import config


def create_user(username: str, password_hash: bytes) -> User:
    with Session(sql_engine) as session:
        new_user: User = User(
            username=username,
            password_hash=password_hash,
            profile_picture_url=config.DEFAULT_PFP_URL
        )

        session.add(new_user)

        try:
            session.commit()
        except IntegrityError:
            session.rollback()

            raise UserAlreadyExistsError

        session.refresh(new_user)

        return new_user


def get_by_username(username: str) -> Optional[User]:
    with Session(sql_engine) as session:
        return session.execute(select(User).where(User.username == username)).scalars().first()
