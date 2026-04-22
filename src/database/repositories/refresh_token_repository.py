from datetime import datetime, timedelta
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database.models import RefreshToken, User
from database.database import sql_engine


def create_refresh_token(user: User, token_hash: str) -> RefreshToken:
    with Session(sql_engine) as session:
        new_refresh_token: RefreshToken = RefreshToken(
            user_id=user.id,
            token_hash=token_hash,
            
        )
