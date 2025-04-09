from typing import Optional

from fastapi import APIRouter, Depends, Query

from api.dependencies.export_dependencies import ExportDependencies
from application.usecase.export_usercase import ExportUseCase
from domain.enum.enums import ExportSubOption
from domain.ports.export_port import ExportInterface

router = APIRouter()


class ExportController:
    @staticmethod
    @router.get("/exportacao/{ano}/{subopcao}")
    def get_export(
            year: Optional[int] = Query(None, description="Year of export data (1970 - 2024)"),
            sub_option: ExportSubOption = Query(None, description="Suboption for the request"),
            scraper: ExportInterface = Depends(ExportDependencies.get_scraper),
    ):
        use_case = ExportUseCase(scraper)
        return use_case.execute(year, sub_option)
