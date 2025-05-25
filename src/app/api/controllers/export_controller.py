from typing import Optional

from fastapi import APIRouter, Depends

from api.dependencies.auth_dependencies import get_current_user
from api.dependencies.scraper_dependencies import ScraperDependencies
from api.docs.query_examples import QueryExamples
from application.usecase.export_usercase import ExportUseCase
from config.logger import logger
from domain.enum.enums import ExportSubOption
from domain.ports.export_port import ExportInterface

router = APIRouter()


class ExportController:
    @staticmethod
    @router.get("/exportacao")
    def get_export(
            year: Optional[int] = QueryExamples.EXPORT_YEAR,
            sub_option: Optional[ExportSubOption] = QueryExamples.EXPORT_SUBOPTION,
            scraper: ExportInterface = Depends(ScraperDependencies.get_export_scraper),
            username: str = Depends(get_current_user)
    ):
        use_case = ExportUseCase(scraper)
        logger.info("Buscando dados de exportação")
        return use_case.execute(year, sub_option)
