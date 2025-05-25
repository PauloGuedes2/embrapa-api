from typing import Optional

from fastapi import APIRouter, Depends

from api.dependencies.auth_dependencies import get_current_user
from api.dependencies.scraper_dependencies import ScraperDependencies
from api.docs.query_examples import QueryExamples
from application.usecase.commercialization_usecase import CommercializationUseCase
from config.logger import logger
from domain.ports.commercialization_port import CommercializationInterface

router = APIRouter()


class CommercializationController:
    @staticmethod
    @router.get("/comercializacao")
    def get_commercialization(
            year: Optional[int] = QueryExamples.COMMERCIALIZATION_YEAR,
            scraper: CommercializationInterface = Depends(ScraperDependencies.get_commercialization_scraper),
            username: str = Depends(get_current_user)
    ):
        use_case = CommercializationUseCase(scraper)
        logger.info("Buscando dados de comercialização")
        return use_case.execute(year)
