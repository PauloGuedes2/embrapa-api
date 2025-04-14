from typing import Optional

from domain.entities.import_entity import ImportEntity
from domain.enum.enums import ImportSubOption
from domain.ports.import_port import ImportInterface


class ImportUseCase:
    def __init__(self, scraper: ImportInterface):
        self.scraper = scraper

    def execute(self, year: Optional[int], sub_option: Optional[ImportSubOption]) -> list[ImportEntity]:
        return self.scraper.fetch_import(year, sub_option)
