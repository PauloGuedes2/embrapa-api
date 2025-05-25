from typing import Optional

from fastapi import APIRouter, Depends

from api.dependencies.auth_dependencies import get_current_user
from api.dependencies.scraper_dependencies import ScraperDependencies
from api.docs.query_examples import QueryExamples
from application.usecase.import_usercase import ImportUseCase
from config.logger import logger
from domain.enum.enums import ImportSubOption
from domain.ports.import_port import ImportInterface

router = APIRouter()


class ImportController:
    @staticmethod
    @router.get("/importacao")
    def get_import(
            year: Optional[int] = QueryExamples.IMPORT_YEAR,
            sub_option: Optional[ImportSubOption] = QueryExamples.IMPORT_SUBOPTION,
            scraper: ImportInterface = Depends(ScraperDependencies.get_import_scraper),
            username: str = Depends(get_current_user)
    ):
        use_case = ImportUseCase(scraper)
        logger.info("Buscando dados de importação")
        return use_case.execute(year, sub_option)
