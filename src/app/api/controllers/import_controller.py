from typing import Optional

from fastapi import APIRouter, Depends, Query

from api.dependencies.auth_dependencies import get_current_user
from api.dependencies.scraper_dependencies import ScraperDependencies
from application.usecase.import_usercase import ImportUseCase
from config.logger import logger
from domain.enum.enums import ImportSubOption
from domain.ports.import_port import ImportInterface

router = APIRouter()


class ImportController:
    @staticmethod
    @router.get("/importacao/{ano}/{subopcao}")
    def get_import(
            year: Optional[int] = Query(None, description="Ano dos dados de importação (1970 - 2024)"),
            sub_option: Optional[ImportSubOption] = Query(None, description="Subopção para a requisição"),
            scraper: ImportInterface = Depends(ScraperDependencies.get_import_scraper),
            username: str = Depends(get_current_user)
    ):
        use_case = ImportUseCase(scraper)
        logger.info("Buscando dados de importação")
        return use_case.execute(year, sub_option)
