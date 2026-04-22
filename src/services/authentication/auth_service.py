from typing import Optional
import bcrypt
import secrets
import string
import config
from datetime import datetime, timedelta
from errors import InvalidCretentialsError
from database.models import User
import database.repositories.user_repository as user_repository
from .AccessCode import AccessCode


def create_user(username: str, password: str) -> User:
    password_hash: bytes = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    return user_repository.create_user(username, password_hash)


access_codes: list[AccessCode] = []


def try_login(username: str, password: str) -> AccessCode:
    user: Optional[User] = user_repository.get_by_username(username)

    if not user:
        raise InvalidCretentialsError("Username not found")

    if not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
        raise InvalidCretentialsError("Incorrect password")

    new_access_code: AccessCode = AccessCode(
        code="".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(config.ACCESS_TOKEN_LENGTH)),
        expires_at=datetime.now() + timedelta(minutes=10),
        user=user
    )

    access_codes.append(new_access_code)

    return new_access_code


def get_tokens(access_code_key: str) -> None:
    for access_code in access_codes:
        if not access_code.code == access_code_key:
            continue

        user: User = access_code.user
