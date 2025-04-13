from adapter.scraper.commercialization_scraper import CommercializationScraper
from adapter.scraper.export_scraper import ExportScraper
from adapter.scraper.import_scraper import ImportScraper
from adapter.scraper.processing_scraper import ProcessingScraper
from adapter.scraper.production_scraper import ProductionScraper
from domain.ports.commercialization_port import CommercializationInterface
from domain.ports.export_port import ExportInterface
from domain.ports.import_port import ImportInterface
from domain.ports.processing_port import ProcessingInterface
from domain.ports.production_port import ProductionInterface


class ScraperDependencies:
    @staticmethod
    def get_export_scraper() -> ExportInterface:
        return ExportScraper()

    @staticmethod
    def get_import_scraper() -> ImportInterface:
        return ImportScraper()

    @staticmethod
    def get_production_scraper() -> ProductionInterface:
        return ProductionScraper()

    @staticmethod
    def get_commercialization_scraper() -> CommercializationInterface:
        return CommercializationScraper()

    @staticmethod
    def get_processing_scraper() -> ProcessingInterface:
        return ProcessingScraper()
