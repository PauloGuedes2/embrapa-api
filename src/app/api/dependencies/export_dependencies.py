from adapter.scraper.export_scraper import ExportScraper
from domain.ports.export_port import ExportInterface


class ExportDependencies:
    @staticmethod
    def get_scraper() -> ExportInterface:
        return ExportScraper()