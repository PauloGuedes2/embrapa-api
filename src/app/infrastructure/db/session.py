import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv

load_dotenv()


class DatabaseSession:
    def __init__(self):
        self.app_env = os.getenv("APP_ENV", "dev")
        self.database_url = self._get_database_url()
        self.engine = create_engine(self.database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    @staticmethod
    def _get_database_url(self) -> str:
        return os.getenv("DATABASE_URL", "sqlite:///./app.db")

    def get_session(self) -> Session:
        return self.SessionLocal()


def get_db():
    db_session = DatabaseSession().get_session()
    try:
        yield db_session
    finally:
        db_session.close()
