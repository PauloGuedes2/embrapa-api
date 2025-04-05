from src.app.domain.entities.producao_entity import ProducaoEntity
from src.app.domain.ports.producao_port import ProducaoInterface



class ProducaoUseCase:
    def __init__(self, scraper: ProducaoInterface):
        self.scraper = scraper
        # self.repository = repository

    # def execute(self, ano: int) -> List[ProducaoEntity]:
    #     producao = self.scraper.buscar_producao(ano)
    #     # self.repository.salvar_producao(producao)
    #     return producao

    def execute(self, ano: int) -> list[ProducaoEntity]:
        return self.scraper.buscar_producao(ano)
