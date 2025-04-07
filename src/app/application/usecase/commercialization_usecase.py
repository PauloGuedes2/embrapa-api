from typing import Optional

from domain.entities.commercialization_entity import CommercializationEntity
from domain.ports.commercialization_port import CommercializationInterface


class CommercializationUseCase:
    def __init__(self, scraper: CommercializationInterface):
        self.scraper = scraper

    def execute(self, year: Optional[int]) -> list[CommercializationEntity]:
        return self.scraper.fetch_commercialization(year)
