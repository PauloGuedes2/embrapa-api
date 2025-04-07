from abc import ABC
from typing import Optional
from adapters.scraper.base_scraper import CommercializationScraperBase
from config.params import BASE_URL, YEAR_QUERY
from domain.entities.commercialization_entity import CommercializationEntity
from domain.ports.commercialization_port import CommercializationInterface
from util.utils import Utils


class CommercializationScraper(CommercializationScraperBase, CommercializationInterface, ABC):
    def __init__(self):
        super().__init__(f"{BASE_URL}?opcao=opt_04")

    def fetch_commercialization(self, year: Optional[int]) -> list[CommercializationEntity]:
        year = Utils.validate_year(year)
        url = self._build_url(self.base_url, year)

        print(f"URL: {url}")
        soup = self.fetch_data(url)

        table = soup.find("table", {"class": "tb_base tb_dados"})
        commercializations = []

        for row in table.find_all("tr")[1:]:
            cols = row.find_all("td")
            product = cols[0].text.strip()
            quantity = cols[1].text.strip()
            commercializations.append(CommercializationEntity(product, quantity))

        return commercializations

    @staticmethod
    def _build_url(base_url: str, year: Optional[int] = None) -> str:
        return base_url if year is None else f"{base_url}{YEAR_QUERY}{year}"
