from fastapi import APIRouter, Depends

from api.dependencies.producao_dependencies import get_scraper
from application.usecase.producao_usecase import ProducaoUseCase
from domain.ports.producao_port import ProducaoInterface

router = APIRouter()

@router.get("/producao/{ano}")
def get_producao(
    ano: int,
    scraper: ProducaoInterface = Depends(get_scraper),
):
    use_case = ProducaoUseCase(scraper)
    return use_case.execute(ano)
