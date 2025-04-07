from abc import ABC
from typing import Optional
from adapters.scraper.base_scraper import ExportScraperBase
from config.params import BASE_URL, YEAR_QUERY
from domain.entities.export_entity import ExportEntity
from domain.ports.export_port import ExportInterface, SubOption
from util.utils import Utils

class ExportScraper(ExportScraperBase, ExportInterface, ABC):
    def __init__(self):
        super().__init__(f"{BASE_URL}")

    def fetch_export(self, year: Optional[int], suboption: SubOption) -> list[ExportEntity]:
        # Valida o ano
        year = Utils.validate_year(year)
        url = self._build_url(self.base_url, year, suboption)

        print(f"URL: {url}")
        soup = self.fetch_data(url)

        table = soup.find("table", {"class": "tb_base tb_dados"})
        exports = []

        for row in table.find_all("tr")[1:]:
            cols = row.find_all("td")
            country = cols[0].text.strip()
            quantity = cols[1].text.strip()
            price = cols[2].text.strip()
            
            # Cria uma instância de ExportEntity e adiciona à lista
            exports.append(ExportEntity(country, quantity, price))
        
        return exports


    @staticmethod
    def _build_url(base_url: str, year: Optional[int], suboption: SubOption) -> str:
        # Adiciona o parâmetro 'ano' se fornecido
        year_param = f"ano={year}" if year is not None else ""
        return f"{base_url}?{year_param}&opcao=opt_06&subopcao={suboption.name}"


