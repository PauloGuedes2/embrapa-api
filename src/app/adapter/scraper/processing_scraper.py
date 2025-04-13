from abc import ABC
from typing import Optional

from adapter.scraper.base_scraper import ProcessingScraperBase
from application.validator.year_validator import YearValidator
from config.params import BASE_URL
from domain.entities.processing_entity import ProcessingEntity
from domain.enum.enums import Option, ProcessingSubOption
from domain.ports.processing_port import ProcessingInterface
from util.utils import Utils


class ProcessingScraper(ProcessingScraperBase, ProcessingInterface, ABC):
    def __init__(self):
        super().__init__(f"{BASE_URL}{Option.PROCESSING.value}")

    def fetch_processing(self, year: Optional[int], sub_option: ProcessingSubOption) -> list[ProcessingEntity]:
        year = YearValidator.validate(self.base_url, year)
        url = Utils.build_url(self.base_url, year, sub_option)
        soup = self.fetch_data(url)

        table_data = Utils.extract_generic_table_data(
            soup=soup,
            table_class="tb_base tb_dados",
            skip_rows=1
        )

        return [ProcessingEntity(cultivate=row[0], amount=row[1]) for row in table_data]
