from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from api.dependencies.db_dependencies import get_db
from adapter.repository.user_repository import UserRepository
from application.usecase.auth_usecase import AuthUseCase

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    auth_usecase = AuthUseCase(user_repo)
    token = auth_usecase.authenticate_user(form_data.username, form_data.password)
    if not token:
        raise HTTPException(status_code=400, detail="Credenciais inválidas ou usuário inativo")
    return {"access_token": token, "token_type": "bearer"}