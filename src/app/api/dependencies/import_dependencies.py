from adapter.scraper.import_scraper import ImportScraper
from domain.ports.import_port import ImportInterface


class ImportDependencies:
    @staticmethod
    def get_scraper() -> ImportInterface:
        return ImportScraper()
