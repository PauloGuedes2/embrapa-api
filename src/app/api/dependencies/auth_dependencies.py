from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from application.service.jwt_service import JWTService
from config.jwt_settings import JWTSettings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/embrapa-vitivinicultura/auth/login")
jwt_service = JWTService(JWTSettings())

def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    try:
        payload = jwt_service.decode_token(token)
        return payload["sub"]
    except (JWTError, KeyError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
