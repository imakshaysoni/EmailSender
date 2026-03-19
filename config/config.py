from enum import Enum
import os
from pydantic import BaseModel

DATABASE_NAME = "notify_service"
PEPPER = os.getenv("PEPPER", "dhpng")

class AdminDetails(Enum):
    EMAIL_ADDRESS = "soniaayush0044@gmail.com"
    USER_NAME = "Aayush Soni"
    SECRET_KEY = "bpwy exxc nkkn eofg"

class AuthTokenConfig(Enum):
    SECRET_KEY = "default-token-key"  # use env in prod
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 1
    REFRESH_TOKEN_EXPIRE_MINUTES = 1

class TokenData(BaseModel):
    username: str | None = None
