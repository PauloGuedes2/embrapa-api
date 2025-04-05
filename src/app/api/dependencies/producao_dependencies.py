from src.app.adapters.scraper.producao_scraper import ProducaoScraper
from src.app.domain.ports.producao_port import ProducaoInterface



def get_scraper() -> ProducaoInterface:
    return ProducaoScraper()
