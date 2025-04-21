from typing import Optional

from fastapi import APIRouter, Depends, Query

from api.dependencies.scraper_dependencies import ScraperDependencies
from application.usecase.production_usecase import ProductionUseCase
from domain.ports.production_port import ProductionInterface
from api.dependencies.auth_dependencies import get_current_user

router = APIRouter()


class ProductionController:
    @staticmethod
    @router.get("/producao/{ano}")
    def get_production(
            year: Optional[int] = Query(None),
            scraper: ProductionInterface = Depends(ScraperDependencies.get_production_scraper),
            username: str = Depends(get_current_user)
    ):
        use_case = ProductionUseCase(scraper)
        return use_case.execute(year)
