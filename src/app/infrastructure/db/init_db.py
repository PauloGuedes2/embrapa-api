from sqlalchemy import inspect

from infrastructure.db.base import Base
from infrastructure.db.session import DatabaseSession


class DatabaseInitializer:
    def __init__(self):
        self.db = DatabaseSession()
        self.engine = self.db.engine
        self.inspector = inspect(self.engine)

    def init_database(self):
        if not self.inspector.has_table("users"):
            print("Criando tabelas do banco de dados...")
            Base.metadata.create_all(bind=self.engine)
        else:
            print("Tabelas já existem.")
