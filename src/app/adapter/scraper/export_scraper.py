from abc import ABC
from typing import Optional

from adapter.scraper.base_scraper import ExportScraperBase
from application.validator.year_validator import YearValidator
from config.params import BASE_URL
from domain.entities.export_entity import ExportEntity
from domain.enum.enums import Option, ExportSubOption
from domain.ports.export_port import ExportInterface
from util.utils import Utils


class ExportScraper(ExportScraperBase, ExportInterface, ABC):
    def __init__(self):
        super().__init__(f"{BASE_URL}{Option.EXPORT.value}")

    def fetch_export(self, year: Optional[int], sub_option: Optional[ExportSubOption]) -> list[ExportEntity]:
        year = YearValidator.validate(self.base_url, year)
        url = Utils.build_url(self.base_url, year, sub_option)
        soup = self.fetch_data(url)

        table_data = Utils.extract_generic_table_data(
            soup=soup,
            table_class="tb_base tb_dados",
            skip_rows=1
        )

        return [ExportEntity(country=row[0], quantity=row[1], value=row[2]) for row in table_data]
