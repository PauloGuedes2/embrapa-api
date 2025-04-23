import uuid
from datetime import timedelta, datetime
from typing import Optional

from jose import jwt, JWTError, ExpiredSignatureError

from config.jwt_settings import JWTSettings
from exceptions.custom_exceptions import InvalidTokenError, ExpiredTokenError


class JWTService:
    def __init__(self, settings: JWTSettings):
        self.settings = settings

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=self.settings.access_token_expire_minutes))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.settings.secret_key, algorithm=self.settings.algorithm)

    def create_refresh_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(days=7))
        to_encode.update({"exp": expire, "jti": str(uuid.uuid4())})
        return jwt.encode(to_encode, self.settings.secret_key, algorithm=self.settings.algorithm)

    def decode_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, self.settings.secret_key, algorithms=[self.settings.algorithm])
            return payload
        except ExpiredSignatureError:
            raise ExpiredTokenError()
        except JWTError:
            raise InvalidTokenError()
