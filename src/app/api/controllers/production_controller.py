from typing import Optional

from fastapi import APIRouter, Depends, Query

from api.dependencies.production_dependencies import ProductionDependencies
from application.usecase.production_usecase import ProductionUseCase
from domain.ports.production_port import ProductionInterface

router = APIRouter()


class ProductionController:
    @staticmethod
    @router.get("/producao/{ano}")
    def get_production(
            year: Optional[int] = Query(None, description="Year of production data (1970 - 2023)"),
            scraper: ProductionInterface = Depends(ProductionDependencies.get_scraper)
    ):

        use_case = ProductionUseCase(scraper)
        return use_case.execute(year)
