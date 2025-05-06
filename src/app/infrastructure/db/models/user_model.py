import uuid

from sqlalchemy import Column, String, UUID

from infrastructure.db.base import Base
from util.utils import Utils


class UserModel(Base):
    current_date = Utils.get_current_utc_brasilia().strftime("%Y-%m-%d %H:%M:%S")

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(200), unique=True, nullable=True)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(String, default=current_date, nullable=False)
