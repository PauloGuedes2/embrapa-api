from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.schemas.auth_schemas import UserRegister, TokenResponse, UserLogin
from application.service.jwt_service import JWTService
from application.service.password_service import PasswordService
from config.jwt_settings import JWTSettings
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
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )

    hashed = password_service.hash_password(user_data.password)
    user = User(
        id=None,
        username=user_data.username,
        email=str(user_data.email),
        hashed_password=hashed,
        created_at=""
    )
    return repo.create_user(user)


@router.post("/auth/login", response_model=TokenResponse)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    repo = AuthRepository(db)
    user = repo.get_user_by_username(user_data.username)

    if not user or not password_service.verify_password(user_data.password, user.hashed_password):
        raise AuthError("Incorrect username or password")

    token = jwt_service.create_access_token({"sub": user.username})
    return TokenResponse(access_token=token, token_type="bearer")
