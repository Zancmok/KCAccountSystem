import os
import dotenv

dotenv.load_dotenv()

# Environment Variables
if (FLASK_SECRET_KEY := os.getenv("FLASK_SECRET_KEY")) is None:
    raise Exception(".env misconfigured!")

if (VERSION := os.getenv("APP_VERSION")) is None:
    raise Exception("Dockerfile does not include a valid version!")

# Flask Config
PORT: int = 5000
HOST: str = "0.0.0.0"
DEBUG: bool = True

# Database Config
MYSQL_PORT: int = 3306
MYSQL_HOST: str = "mysql"
MYSQL_DATABASE: str = "database"
MYSQL_ROOT_PASSWORD: str = "admin"
MYSQL_PASSWORD: str = "admin"
MYSQL_USER: str = "admin"
DATABASE_RECONNECTION_TIMEOUT: float = 1.0

# Account Config
DEFAULT_PFP_URL: str = "https://cdn.discordapp.com/embed/avatars/0.png"

# Access Tokens
ACCESS_TOKEN_LENGTH: int = 60
