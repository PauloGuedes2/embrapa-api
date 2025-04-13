from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from api.controllers.import_controller import ImportController
from domain.enum.enums import ImportSubOption


class TestImportController:
    def test_get_import_success(self):
        mock_scraper = Mock()
        mock_use_case = Mock()
        mock_use_case.execute.return_value = {"data": "import"}

        year = 2020
        sub_option = ImportSubOption.subopt_01

        with patch('api.controllers.import_controller.ImportUseCase', return_value=mock_use_case):
            result = ImportController.get_import(
                year=year,
                sub_option=sub_option,
                scraper=mock_scraper
            )

        mock_use_case.execute.assert_called_once_with(year, sub_option)
        assert result == {"data": "import"}

    def test_get_import_invalid_year(self):
        mock_scraper = Mock()
        mock_scraper.fetch_import.side_effect = HTTPException(status_code=400,
                                                              detail="Invalid year. Must be between 1970 and 2024")
        year = 1800
        sub_option = ImportSubOption.subopt_02

        with pytest.raises(HTTPException) as exc_info:
            ImportController.get_import(
                year=year,
                sub_option=sub_option,
                scraper=mock_scraper
            )

        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Invalid year. Must be between 1970 and 2024"
