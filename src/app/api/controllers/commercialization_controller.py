from typing import Optional

from fastapi import APIRouter, Depends, Query

from api.dependencies.commercialization_dependencies import CommercializationDependencies
from application.usecase.commercialization_usecase import CommercializationUseCase
from domain.ports.commercialization_port import CommercializationInterface

router = APIRouter()


class CommercializationController:
    @staticmethod
    @router.get("/comercializacao/{ano}")
    def get_commercialization(
            year: Optional[int] = Query(None, description="Year of commercialization data (1970 - 2023)"),
            scraper: CommercializationInterface = Depends(CommercializationDependencies.get_scraper)
    ):

        use_case = CommercializationUseCase(scraper)
        return use_case.execute(year)
