from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from api.controllers.production_controller import ProductionController


class TestProductionController:
    def test_get_production_success(self):
        mock_scraper = Mock()
        mock_use_case = Mock()
        mock_use_case.execute.return_value = {"data": "production"}

        year = 2020

        with patch('api.controllers.production_controller.ProductionUseCase', return_value=mock_use_case):
            result = ProductionController.get_production(
                year=year,
                scraper=mock_scraper
            )

        mock_use_case.execute.assert_called_once_with(year)
        assert result == {"data": "production"}

    def test_get_commercialization_invalid_year(self):
        mock_scraper = Mock()
        mock_scraper.fetch_production.side_effect = HTTPException(
            status_code=400,
            detail="Year must be between 1970 and 2023"
        )
        year = 3000

        with pytest.raises(HTTPException) as exc_info:
            ProductionController.get_production(
                year=year,
                scraper=mock_scraper
            )

        assert exc_info.value.status_code == 400
        assert "Year must be between 1970 and 2023" in exc_info.value.detail
