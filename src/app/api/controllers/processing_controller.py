from typing import Optional

from fastapi import APIRouter, Depends

from api.dependencies.auth_dependencies import get_current_user
from api.dependencies.scraper_dependencies import ScraperDependencies
from api.docs.query_examples import QueryExamples
from application.usecase.processing_usecase import ProcessingUseCase
from config.logger import logger
from domain.enum.enums import ProcessingSubOption
from domain.ports.processing_port import ProcessingInterface

router = APIRouter()


class ProcessingController:
    @staticmethod
    @router.get("/processamento")
    def get_processing(
            year: Optional[int] = QueryExamples.PROCESSING_YEAR,
            sub_option: Optional[ProcessingSubOption] = QueryExamples.PROCESSING_SUBOPTION,
            scraper: ProcessingInterface = Depends(ScraperDependencies.get_processing_scraper),
            username: str = Depends(get_current_user)
    ):
        use_case = ProcessingUseCase(scraper)
        logger.info("Buscando dados de processamento")
        return use_case.execute(year, sub_option)
