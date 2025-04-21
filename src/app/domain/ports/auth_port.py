from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.user_entity import User


class AuthRepositoryInterface(ABC):
    @abstractmethod
    def get_user_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass
