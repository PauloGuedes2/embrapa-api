from typing import Optional

from domain.entities.production_entity import ProductionEntity
from domain.ports.production_port import ProductionInterface


class ProductionUseCase:
    def __init__(self, scraper: ProductionInterface):
        self.scraper = scraper

    def execute(self, year: Optional[int]) -> list[ProductionEntity]:
        return self.scraper.fetch_production(year)
