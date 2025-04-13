from abc import ABC
from typing import Optional

from adapter.scraper.base_scraper import ProductionScraperBase
from application.validator.year_validator import YearValidator
from config.params import BASE_URL
from domain.entities.production_entity import ProductionEntity
from domain.enum.enums import Option
from domain.ports.production_port import ProductionInterface
from util.utils import Utils


class ProductionScraper(ProductionScraperBase, ProductionInterface, ABC):
    def __init__(self):
        super().__init__(f"{BASE_URL}{Option.PRODUCTION.value}")

    def fetch_production(self, year: Optional[int]) -> list[ProductionEntity]:
        year = YearValidator.validate(self.base_url, year)
        url = Utils.build_url(self.base_url, year)
        soup = self.fetch_data(url)

        table_data = Utils.extract_generic_table_data(
            soup=soup,
            table_class="tb_base tb_dados",
            skip_rows=1
        )

        return [ProductionEntity(product=row[0], quantity=row[1]) for row in table_data]
