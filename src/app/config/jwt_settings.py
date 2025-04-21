import os
from dotenv import load_dotenv

load_dotenv()

class JWTSettings:
    secret_key: str = os.getenv("JWT_SECRET_KEY", "supersecret")
    algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("JWT_EXPIRE_MINUTES", "30"))