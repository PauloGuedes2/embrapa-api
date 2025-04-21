from datetime import datetime, timedelta
from jose import jwt, JWTError
from typing import Optional

from config.jwt_settings import JWTSettings


class JWTService:
    def __init__(self, settings: JWTSettings):
        self.settings = settings

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=self.settings.access_token_expire_minutes))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.settings.secret_key, algorithm=self.settings.algorithm)

    def decode_token(self, token: str) -> dict:
        try:
            return jwt.decode(token, self.settings.secret_key, algorithms=[self.settings.algorithm])
        except JWTError as e:
            raise ValueError("Token inválido ou expirado") from e
