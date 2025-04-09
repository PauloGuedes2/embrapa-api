from typing import Optional

from domain.entities.export_entity import ExportEntity
from domain.enum.enums import ExportSubOption
from domain.ports.export_port import ExportInterface


class ExportUseCase:
    def __init__(self, scraper: ExportInterface):
        self.scraper = scraper

    def execute(self, year: Optional[int], sub_option: ExportSubOption) -> list[ExportEntity]:
        return self.scraper.fetch_export(year, sub_option)
