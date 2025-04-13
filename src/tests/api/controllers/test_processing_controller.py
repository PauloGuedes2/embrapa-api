from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from api.controllers.processing_controller import ProcessingController
from domain.enum.enums import ProcessingSubOption


class TestProcessingController:
    def test_get_processing_success(self):
        mock_scraper = Mock()
        mock_use_case = Mock()
        mock_use_case.execute.return_value = {"data": "processing"}

        year = 2020
        sub_option = ProcessingSubOption.subopt_01

        with patch('api.controllers.processing_controller.ProcessingUseCase', return_value=mock_use_case):
            result = ProcessingController.get_processing(
                year=year,
                sub_option=sub_option,
                scraper=mock_scraper
            )

        mock_use_case.execute.assert_called_once_with(year, sub_option)
        assert result == {"data": "processing"}

    def test_get_processing_missing_sub_option(self):
        mock_scraper = Mock()
        mock_use_case = Mock()
        mock_use_case.execute.return_value = {"data": "processing"}

        year = 2020

        with patch('api.controllers.processing_controller.ProcessingUseCase', return_value=mock_use_case):
            result = ProcessingController.get_processing(
                year=year,
                sub_option=None,
                scraper=mock_scraper
            )

        mock_use_case.execute.assert_called_once_with(year, None)
        assert result == {"data": "processing"}

    def test_get_processing_invalid_year(self):
        mock_scraper = Mock()
        mock_scraper.fetch_processing.side_effect = HTTPException(status_code=400,
                                                              detail="Invalid year. Must be between 1970 and 2024")
        year = 1800
        sub_option = ProcessingSubOption.subopt_02

        with pytest.raises(HTTPException) as exc_info:
            ProcessingController.get_processing(
                year=year,
                sub_option=sub_option,
                scraper=mock_scraper
            )

        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Invalid year. Must be between 1970 and 2024"
