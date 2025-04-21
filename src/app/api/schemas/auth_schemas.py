from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    username: str
    password: str

class UserRegister(UserLogin):
    email: EmailStr

class TokenResponse(BaseModel):
    access_token: str
    token_type: str