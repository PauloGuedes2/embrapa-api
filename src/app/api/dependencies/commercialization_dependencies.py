from adapter.scraper.commercialization_scraper import CommercializationScraper
from domain.ports.commercialization_port import CommercializationInterface


class CommercializationDependencies:
    @staticmethod
    def get_scraper() -> CommercializationInterface:
        return CommercializationScraper()