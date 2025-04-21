from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from application.service.jwt_service import JWTService
from application.service.password_service import PasswordService
from config.jwt_settings import JWTSettings
from domain.entities.user_entity import User
from infrastructure.db.session import get_db
from infrastructure.db.repositories.auth_repository import AuthRepository
from api.schemas.auth_schemas import UserLogin, UserRegister, TokenResponse

router = APIRouter()
settings = JWTSettings()
jwt_service = JWTService(settings)
password_service = PasswordService()

@router.post("/auth/register", response_model=User)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    repo = AuthRepository(db)
    if repo.get_user_by_username(user_data.username):
        raise HTTPException(status_code=400, detail="Usuário já existe")

    hashed = password_service.hash_password(user_data.password)
    user = User(id=None, username=user_data.username, email=user_data.email, hashed_password=hashed, created_at="")
    return repo.create_user(user)

@router.post("/auth/login", response_model=TokenResponse)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    repo = AuthRepository(db)
    user = repo.get_user_by_username(user_data.username)
    if not user or not password_service.verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = jwt_service.create_access_token({"sub": user.username})
    return TokenResponse(access_token=token, token_type="bearer")
