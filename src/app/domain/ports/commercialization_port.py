from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities.commercialization_entity import CommercializationEntity


class CommercializationInterface(ABC):
    @abstractmethod
    def fetch_commercialization(self, year: Optional[int]) -> List[CommercializationEntity]: ...
