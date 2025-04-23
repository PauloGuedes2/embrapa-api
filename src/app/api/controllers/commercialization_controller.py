from typing import Optional

from fastapi import APIRouter, Depends, Query

from api.dependencies.auth_dependencies import get_current_user
from api.dependencies.scraper_dependencies import ScraperDependencies
from application.usecase.commercialization_usecase import CommercializationUseCase
from domain.ports.commercialization_port import CommercializationInterface

router = APIRouter()


class CommercializationController:
    @staticmethod
    @router.get("/comercializacao/{ano}")
    def get_commercialization(
            year: Optional[int] = Query(None, description="Year of commercialization data (1970 - 2023)"),
            scraper: CommercializationInterface = Depends(ScraperDependencies.get_commercialization_scraper),
            username: str = Depends(get_current_user)
    ):
        use_case = CommercializationUseCase(scraper)
        return use_case.execute(year)
