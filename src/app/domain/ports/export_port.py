from abc import ABC, abstractmethod
from typing import List, Optional
from enum import Enum

from domain.entities.export_entity import ExportEntity


class ExportInterface(ABC):
    @abstractmethod
    def fetch_export(self, year: Optional[int]) -> List[ExportEntity]: ...


class SubOption(str, Enum):
    subopt_01 = "Vinhos de mesa"
    subopt_02 = "Espumantes"
    subopt_03 = "Uvas frescas"
    subopt_04 = "Suco de uva"