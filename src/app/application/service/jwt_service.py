from datetime import timedelta
from typing import Optional

from jose import jwt, JWTError, ExpiredSignatureError

from config.jwt_settings import JWTSettings
from exceptions.custom_exceptions import InvalidTokenError, ExpiredTokenError
from util.utils import Utils


class JWTService:
    def __init__(self, settings: JWTSettings):
        self.settings = settings

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        expire = Utils.get_current_utc_brasilia() + (expires_delta or timedelta(minutes=self.settings.access_token_expire_minutes))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.settings.secret_key, algorithm=self.settings.algorithm)

    def decode_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, self.settings.secret_key, algorithms=[self.settings.algorithm])
            return payload
        except ExpiredSignatureError:
            raise ExpiredTokenError()
        except JWTError:
            raise InvalidTokenError()
