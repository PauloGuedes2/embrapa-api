from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities.export_entity import ExportEntity
from domain.enum.enums import ExportSubOption


class ExportInterface(ABC):
    @abstractmethod
    def fetch_export(self, year: Optional[int], sub_option: Optional[ExportSubOption]) -> List[ExportEntity]: ...
