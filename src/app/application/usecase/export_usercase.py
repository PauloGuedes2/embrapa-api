from typing import Optional

from domain.entities.export_entity import ExportEntity
from domain.ports.export_port import ExportInterface, SubOption


class ExportUseCase:
    def __init__(self, scraper: ExportInterface):
        self.scraper = scraper

    def execute(self, year: Optional[int], suboption: SubOption) -> list[ExportEntity]:
        return self.scraper.fetch_export(year, suboption)
