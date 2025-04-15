from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "tb_contas"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String, unique=True, index=True, nullable=False)
    hash_password = Column(String, nullable=False)
    mail = Column(String, nullable=False)
    stats = Column(Boolean, default=True)
    access_role = Column(String, default="user")
    create_date = Column(DateTime, default=datetime.utcnow) 
    last_update = Column(DateTime, default=datetime.utcnow)