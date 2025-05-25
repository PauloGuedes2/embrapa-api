from typing import Optional

from fastapi import APIRouter, Depends, Query

from api.dependencies.auth_dependencies import get_current_user
from api.dependencies.scraper_dependencies import ScraperDependencies
from application.usecase.production_usecase import ProductionUseCase
from config.logger import logger
from domain.ports.production_port import ProductionInterface

router = APIRouter()


class ProductionController:
    @staticmethod
    @router.get("/producao")
    def get_production(
            year: Optional[int] = Query(None, description="Ano dos dados de produção (1970 - 2023)"),
            scraper: ProductionInterface = Depends(ScraperDependencies.get_production_scraper),
            username: str = Depends(get_current_user)
    ):
        use_case = ProductionUseCase(scraper)
        logger.info("Buscando dados de produção")
        return use_case.execute(year)
