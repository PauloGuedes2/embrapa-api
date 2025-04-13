from typing import Optional
from fastapi import APIRouter, Depends, Query
from domain.enum.enums import ProcessingSubOption
from domain.ports.processing_port import ProcessingInterface
from application.usecase.processing_usecase import ProcessingUseCase
from api.dependencies.processing_dependencies import ProcessingDependencies


router = APIRouter()


class ProcessingController:
    @staticmethod
    @router.get("/processamento/{ano}/{subopcao}")
    def get_processing(
            year: Optional[int] = Query(None, description="Year of export data (1970 - 2024)"),
            sub_option: ProcessingSubOption = Query(None, description="Suboption for the request"),
            scraper: ProcessingInterface = Depends(ProcessingDependencies.get_scraper),
    ):
        use_case = ProcessingUseCase(scraper)
        return use_case.execute(year, sub_option)
