from abc import ABC
from typing import Optional

from adapters.scraper.base_scraper import CommercializationScraperBase
from application.validator.year_validator import YearValidator
from config.params import BASE_URL
from domain.entities.commercialization_entity import CommercializationEntity
from domain.enum.enums import Option
from domain.ports.commercialization_port import CommercializationInterface
from util.utils import Utils


class CommercializationScraper(CommercializationScraperBase, CommercializationInterface, ABC):
    def __init__(self):
        super().__init__(f"{BASE_URL}{Option.COMMERCIALIZATION.value}")

    def fetch_commercialization(self, year: Optional[int]) -> list[CommercializationEntity]:
        year = YearValidator.validate(self.base_url, year)
        url = Utils.build_url(self.base_url, year)
        soup = self.fetch_data(url)

        table_data = Utils.extract_generic_table_data(
            soup=soup,
            table_class="tb_base tb_dados",
            skip_rows=1
        )

        return [CommercializationEntity(product=row[0], quantity=row[1]) for row in table_data]
