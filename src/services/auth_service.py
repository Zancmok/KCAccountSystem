import bcrypt
from database.models import User
import database.repositories.user_repository as user_repository


def create_user(username: str, password: str) -> User:
    password_hash: bytes = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    return user_repository.create_user(username, password_hash)
