from typing import Optional

from fastapi import APIRouter, Depends, Query

from api.dependencies.auth_dependencies import get_current_user
from api.dependencies.scraper_dependencies import ScraperDependencies
from application.usecase.export_usercase import ExportUseCase
from config.logger import logger
from domain.enum.enums import ExportSubOption
from domain.ports.export_port import ExportInterface

router = APIRouter()


class ExportController:
    @staticmethod
    @router.get("/exportacao")
    def get_export(
            year: Optional[int] = Query(None, description="Ano dos dados de exportação (1970 - 2024)"),
            sub_option: Optional[ExportSubOption] = Query(None, description="Subopção para a requisição"),
            scraper: ExportInterface = Depends(ScraperDependencies.get_export_scraper),
            username: str = Depends(get_current_user)
    ):
        use_case = ExportUseCase(scraper)
        logger.info("Buscando dados de exportação")
        return use_case.execute(year, sub_option)
