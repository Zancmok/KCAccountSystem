from dataclasses import dataclass
from datetime import datetime
from database.models.User import User


@dataclass
class AccessToken:
    code: str
    expires_at: datetime
    user: User
