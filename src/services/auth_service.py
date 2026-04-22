from typing import Optional
import bcrypt
import secrets
import string
import config
from datetime import datetime, timedelta
from errors import InvalidCretentialsError
from database.models import User
import database.repositories.user_repository as user_repository
from .AccessToken import AccessToken


def create_user(username: str, password: str) -> User:
    password_hash: bytes = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    return user_repository.create_user(username, password_hash)


access_tokens: list[AccessToken] = []


def try_login(username: str, password: str) -> AccessToken:
    user: Optional[User] = user_repository.get_by_username(username)

    if not user:
        raise InvalidCretentialsError("Username not found")

    if not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
        raise InvalidCretentialsError("Incorrect password")

    new_access_token: AccessToken = AccessToken(
        code="".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(config.ACCESS_TOKEN_LENGTH)),
        expires_at=datetime.now() + timedelta(minutes=10),
        user=user
    )

    access_tokens.append(new_access_token)

    return new_access_token
