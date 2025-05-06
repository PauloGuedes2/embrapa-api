from typing import Optional

from fastapi import APIRouter, Depends, Query

from api.dependencies.auth_dependencies import get_current_user
from api.dependencies.scraper_dependencies import ScraperDependencies
from application.usecase.processing_usecase import ProcessingUseCase
from config.logger import logger
from domain.enum.enums import ProcessingSubOption
from domain.ports.processing_port import ProcessingInterface

router = APIRouter()


class ProcessingController:
    @staticmethod
    @router.get("/processamento/{ano}/{subopcao}")
    def get_processing(
            year: Optional[int] = Query(None, description="Ano dos dados de processamento (1970 - 2024)"),
            sub_option: Optional[ProcessingSubOption] = Query(None, description="Subopção para a requisição"),
            scraper: ProcessingInterface = Depends(ScraperDependencies.get_processing_scraper),
            username: str = Depends(get_current_user)
    ):
        use_case = ProcessingUseCase(scraper)
        logger.info("Buscando dados de processamento")
        return use_case.execute(year, sub_option)
