from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from api.controllers.commercialization_controller import CommercializationController


class TestCommercializationController:
    def test_get_commercialization_success(self):
        mock_scraper = Mock()
        mock_use_case = Mock()
        mock_use_case.execute.return_value = {"data": "commercialization"}

        year = 2020

        with patch('api.controllers.commercialization_controller.CommercializationUseCase', return_value=mock_use_case):
            result = CommercializationController.get_commercialization(
                year=year,
                scraper=mock_scraper
            )

        mock_use_case.execute.assert_called_once_with(year)
        assert result == {"data": "commercialization"}

    def test_get_commercialization_invalid_year(self):
        mock_scraper = Mock()
        mock_scraper.fetch_commercialization.side_effect = HTTPException(
            status_code=400,
            detail="Year must be between 1970 and 2023"
        )
        year = 3000

        with pytest.raises(HTTPException) as exc_info:
            CommercializationController.get_commercialization(
                year=year,
                scraper=mock_scraper
            )

        assert exc_info.value.status_code == 400
        assert "Year must be between 1970 and 2023" in exc_info.value.detail