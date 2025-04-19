from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

from util.utils import Utils

Base = declarative_base()


class User(Base):
    current_date = Utils.get_current_utc_brasilia().strftime("%Y-%m-%d %H:%M:%S")

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    refresh_token = Column(Text)
    created_at = Column(DateTime, default=current_date, nullable=False)