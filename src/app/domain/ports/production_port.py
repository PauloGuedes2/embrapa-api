from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities.production_entity import ProductionEntity


class ProductionInterface(ABC):
    @abstractmethod
    def fetch_production(self, year: Optional[int]) -> List[ProductionEntity]: ...
