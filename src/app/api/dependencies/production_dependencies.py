from adapters.scraper.production_scraper import ProductionScraper
from domain.ports.production_port import ProductionInterface


class ProductionDependencies:
    @staticmethod
    def get_scraper() -> ProductionInterface:
        return ProductionScraper()