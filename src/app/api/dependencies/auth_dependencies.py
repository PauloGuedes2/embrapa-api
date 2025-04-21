from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from application.service.jwt_service import JWTService
from config.jwt_settings import JWTSettings
from config.params import ROUTER_PREFIX
from exceptions.custom_exceptions import InvalidTokenError, ExpiredTokenError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{ROUTER_PREFIX}/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    jwt_service = JWTService(JWTSettings())
    try:
        payload = jwt_service.decode_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise InvalidTokenError()
        return username
    except (InvalidTokenError, ExpiredTokenError) as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
