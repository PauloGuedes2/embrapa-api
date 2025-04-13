from typing import List, Optional
from abc import ABC, abstractmethod
from domain.enum.enums import ProcessingSubOption
from domain.entities.processing_entity import ProcessingEntity


class ProcessingInterface(ABC):
    @abstractmethod
    def fetch_processing(self, year: Optional[int], sub_option: Optional[ProcessingSubOption]) -> List[ProcessingEntity]: ...
