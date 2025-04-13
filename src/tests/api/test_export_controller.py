from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from api.controllers.export_controller import ExportController
from domain.enum.enums import ExportSubOption


class TestExportController:
    def test_get_export_success(self):
        mock_scraper = Mock()
        mock_use_case = Mock()
        mock_use_case.execute.return_value = {"data": "export"}

        year = 2020
        sub_option = ExportSubOption.subopt_01

        with patch('api.controllers.export_controller.ExportUseCase', return_value=mock_use_case):
            result = ExportController.get_export(
                year=year,
                sub_option=sub_option,
                scraper=mock_scraper
            )

        mock_use_case.execute.assert_called_once_with(year, sub_option)
        assert result == {"data": "export"}

    def test_get_export_missing_sub_option(self):
        mock_scraper = Mock()
        mock_use_case = Mock()
        mock_use_case.execute.return_value = {"data": "export"}

        year = 2020

        with patch('api.controllers.export_controller.ExportUseCase', return_value=mock_use_case):
            result = ExportController.get_export(
                year=year,
                sub_option=None,
                scraper=mock_scraper
            )

        mock_use_case.execute.assert_called_once_with(year, None)
        assert result == {"data": "export"}

    def test_get_export_invalid_year(self):
        mock_scraper = Mock()
        mock_scraper.fetch_export.side_effect = HTTPException(status_code=400,
                                                              detail="Invalid year. Must be between 1970 and 2024")

        year = 1800
        sub_option = ExportSubOption.subopt_01

        with pytest.raises(HTTPException) as exc_info:
            ExportController.get_export(
                year=year,
                sub_option=sub_option,
                scraper=mock_scraper
            )

        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Invalid year. Must be between 1970 and 2024"