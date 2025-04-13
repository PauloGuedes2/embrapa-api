from domain.ports.processing_port import ProcessingInterface
from adapters.scraper.processing_scraper import ProcessingScraper


class ProcessingDependencies:
    @staticmethod
    def get_scraper() -> ProcessingInterface:
        return ProcessingScraper()