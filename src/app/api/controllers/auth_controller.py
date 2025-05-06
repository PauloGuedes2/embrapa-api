from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.schemas.auth_schemas import UserRegister, TokenResponse, UserLogin
from application.service.jwt_service import JWTService
from application.service.password_service import PasswordService
from config.jwt_settings import JWTSettings
from config.logger import logger
from domain.entities.user_entity import User
from exceptions.custom_exceptions import AuthError
from infrastructure.db.repositories.auth_repository import AuthRepository
from infrastructure.db.session import get_db

router = APIRouter()
settings = JWTSettings()
jwt_service = JWTService(settings)
password_service = PasswordService()


@router.post("/auth/register", response_model=User)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    repo = AuthRepository(db)
    if repo.get_user_by_username(user_data.username):
        logger.warning(f"Usuário já existe: {user_data.username}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário já registrado"
        )

    hashed = password_service.hash_password(user_data.password)
    user = User(
        id=None,
        username=user_data.username,
        email=str(user_data.email),
        hashed_password=hashed,
        created_at=""
    )

    logger.info(f"Criando novo usuário: {user_data.username}")
    return repo.create_user(user)


@router.post("/auth/login", response_model=TokenResponse)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    repo = AuthRepository(db)
    logger.info(f"Tentativa de login para: {user_data.username}")
    user = repo.get_user_by_username(user_data.username)

    if not user or not password_service.verify_password(user_data.password, user.hashed_password):
        logger.warning(f"Falha no login para: {user_data.username}")
        raise AuthError

    token = jwt_service.create_access_token({"sub": user.username})
    refresh_token = jwt_service.create_refresh_token({"sub": user.username})
    logger.info(f"Login bem-sucedido para: {user_data.username}")
    return TokenResponse(access_token=token, refresh_token=refresh_token, token_type="bearer")
