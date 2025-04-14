from typing import Optional

from fastapi import APIRouter, Depends, Query

from api.dependencies.scraper_dependencies import ScraperDependencies
from application.usecase.import_usercase import ImportUseCase
from domain.enum.enums import ImportSubOption
from domain.ports.import_port import ImportInterface

router = APIRouter()


class ImportController:
    @staticmethod
    @router.get("/importacao/{ano}/{subopcao}")
    def get_import(
            year: Optional[int] = Query(None, description="Year of import data (1970 - 2024)"),
            sub_option: Optional[ImportSubOption] = Query(None, description="Suboption for the request"),
            scraper: ImportInterface = Depends(ScraperDependencies.get_import_scraper),
    ):
        use_case = ImportUseCase(scraper)
        return use_case.execute(year, sub_option)
