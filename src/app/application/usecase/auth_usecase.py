from adapter.repository.user_repository import UserRepository
from adapter.security.jwt_service import verify_password, create_access_token

class AuthUseCase:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def authenticate_user(self, username: str, password: str):
        user = self.user_repo.get_by_username(username)
        if not user or not verify_password(password, user.hash_password):
            return None
        if not user.stats:
            return None

        token_data = {
            "sub": user.usuario,
            "role": user.access_role,
            "date_create": user.create_date.isoformat()
        }
        return create_access_token(token_data)