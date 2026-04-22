from typing import Optional
import bcrypt
from errors import InvalidCretentialsError
from database.models import User
import database.repositories.user_repository as user_repository


def create_user(username: str, password: str) -> User:
    password_hash: bytes = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    return user_repository.create_user(username, password_hash)


def try_login(username: str, password: str) -> User:
    user: Optional[User] = user_repository.get_by_username(username)

    if not user:
        raise InvalidCretentialsError

    if not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
        raise InvalidCretentialsError

    return user
