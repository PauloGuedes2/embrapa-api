from fastapi import FastAPI, Depends

from api.dependencies.producao_dependencies import get_scraper
from application.usecase.producao_usecase import ProducaoUseCase
from domain.ports.producao_port import ProducaoInterface

app = FastAPI()

@app.get("/producao/{ano}")
def get_producao(
    ano: int,
    scraper: ProducaoInterface = Depends(get_scraper),
    # repository: IRepository = Depends(get_repository)
):
    # use_case = ObterProducaoUseCase(scraper, repository)
    use_case = ProducaoUseCase(scraper)
    return use_case.execute(ano)