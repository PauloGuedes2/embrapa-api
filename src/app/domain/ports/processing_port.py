from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities.processing_entity import ProcessingEntity
from domain.enum.enums import ProcessingSubOption


class ProcessingInterface(ABC):
    @abstractmethod
    def fetch_processing(self, year: Optional[int], sub_option: Optional[ProcessingSubOption]) -> List[ProcessingEntity]: ...
