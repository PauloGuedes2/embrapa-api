from abc import ABC, abstractmethod
from typing import Optional, List

from domain.entities.import_entity import ImportEntity
from domain.enum.enums import ImportSubOption


class ImportInterface(ABC):
    @abstractmethod
    def fetch_import(self, year: Optional[int], sub_option: Optional[ImportSubOption]) -> List[ImportEntity]: ...
