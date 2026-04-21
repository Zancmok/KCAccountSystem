import bcrypt
from database.models import User
import database.repositories.user_repository


def create_user(username: str, password: str) -> None:
    password_hash: bytes = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )


