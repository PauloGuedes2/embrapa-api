from typing import Optional
from domain.enum.enums import ProcessingSubOption
from domain.ports.processing_port import ProcessingInterface
from domain.entities.processing_entity import ProcessingEntity


class ProcessingUseCase:
    def __init__(self, scraper: ProcessingInterface):
        self.scraper = scraper

    def execute(self, year: Optional[int], sub_option: Optional[ProcessingSubOption]) -> list[ProcessingEntity]:
        return self.scraper.fetch_processing(year, sub_option)
