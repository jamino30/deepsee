from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from deepsee.backend.app.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(
    subject: str, expires_delta: timedelta | None = None
) -> str:
    """
    Creates an access token.
    """
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {'exp': expire, 'sub': str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify password.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Get hashed password.
    """
    return pwd_context.hash(password)