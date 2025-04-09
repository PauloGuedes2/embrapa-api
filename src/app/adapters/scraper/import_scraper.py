from abc import ABC
from typing import Optional

from adapters.scraper.base_scraper import ImportScraperBase
from application.validator.year_validator import YearValidator
from config.params import BASE_URL
from domain.entities.import_entity import ImportEntity
from domain.enum.enums import Option, ImportSubOption
from domain.ports.import_port import ImportInterface
from util.utils import Utils


class ImportScraper(ImportScraperBase, ImportInterface, ABC):
    def __init__(self):
        super().__init__(f"{BASE_URL}{Option.IMPORT.value}")

    def fetch_import(self, year: Optional[int], sub_option: Optional[ImportSubOption]) -> list[ImportEntity]:
        year = YearValidator.validate(self.base_url, year)
        url = Utils.build_url(self.base_url, year, sub_option)
        soup = self.fetch_data(url)

        table_data = Utils.extract_generic_table_data(
            soup=soup,
            table_class="tb_base tb_dados",
            skip_rows=1
        )

        return [ImportEntity(country=row[0], quantity=row[1], value=row[2]) for row in table_data]
