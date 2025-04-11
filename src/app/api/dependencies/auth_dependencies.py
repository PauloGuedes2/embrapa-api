from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from adapters.security.jwt_service import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token invÃ¡lido")
    return payload  # retorna os dados do token (sub, role, data_cadastro)