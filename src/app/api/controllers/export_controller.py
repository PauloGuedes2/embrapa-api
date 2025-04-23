from typing import Optional

from fastapi import APIRouter, Depends, Query

from api.dependencies.auth_dependencies import get_current_user
from api.dependencies.scraper_dependencies import ScraperDependencies
from application.usecase.export_usercase import ExportUseCase
from domain.enum.enums import ExportSubOption
from domain.ports.export_port import ExportInterface

router = APIRouter()


class ExportController:
    @staticmethod
    @router.get("/exportacao/{ano}/{subopcao}")
    def get_export(
            year: Optional[int] = Query(None, description="Year of export data (1970 - 2024)"),
            sub_option: Optional[ExportSubOption] = Query(None, description="Suboption for the request"),
            scraper: ExportInterface = Depends(ScraperDependencies.get_export_scraper),
            username: str = Depends(get_current_user)
    ):
        use_case = ExportUseCase(scraper)
        return use_case.execute(year, sub_option)
