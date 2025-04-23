from typing import Optional

from sqlalchemy.orm import Session

from domain.entities.user_entity import User
from domain.ports.auth_port import AuthRepositoryInterface
from infrastructure.db.models.user_model import UserModel


class AuthRepository(AuthRepositoryInterface):
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_username(self, username: str) -> Optional[User]:
        user_model: Optional[UserModel] = self.session.query(UserModel).filter_by(username=username).first()
        if user_model is not None:
            return self._to_entity(user_model)
        return None

    def create_user(self, user: User) -> User:
        user_model = UserModel(
            username=user.username,
            hashed_password=user.hashed_password
        )
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)
        return self._to_entity(user_model)

    @staticmethod
    def _to_entity(model: UserModel) -> User:
        return User(
            id=model.id,
            username=model.username,
            email=model.email,
            hashed_password=model.hashed_password,
            created_at=model.created_at if model.created_at else None
        )
