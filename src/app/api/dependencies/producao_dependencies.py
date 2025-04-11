from adapters.scraper.producao_scraper import ProducaoScraper
from domain.ports.producao_port import ProducaoInterface



def get_scraper() -> ProducaoInterface:
    return ProducaoScraper()
