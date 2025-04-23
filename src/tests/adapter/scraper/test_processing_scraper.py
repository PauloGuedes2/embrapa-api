from unittest.mock import patch, MagicMock

import pytest

from adapter.scraper.processing_scraper import ProcessingScraper
from domain.entities.processing_entity import ProcessingEntity
from domain.enum.enums import ProcessingSubOption

HTTP_FAKE = "http://fakeurl.com"


class TestProcessingScraper:
    def test_fetch_processing_returns_entities_for_valid_year_and_sub_option(self):
        mock_soup = MagicMock()
        mock_table_data = [["Cultivo A", "100"], ["Cultivo B", "200"]]

        with patch("adapter.scraper.base_scraper.BaseScraper.fetch_data", return_value=mock_soup), \
                patch("util.utils.Utils.extract_generic_table_data", return_value=mock_table_data), \
                patch("application.validator.year_validator.YearValidator.validate", return_value=2021), \
                patch("util.utils.Utils.build_url", return_value=HTTP_FAKE):
            scraper = ProcessingScraper()
            result = scraper.fetch_processing(2021, ProcessingSubOption.subopt_01)

            assert len(result) == 2
            assert isinstance(result[0], ProcessingEntity)
            assert result[0].cultivate == "Cultivo A"
            assert result[0].amount == "100"
            assert result[1].cultivate == "Cultivo B"
            assert result[1].amount == "200"

    def test_fetch_processing_raises_error_for_invalid_year(self):
        with patch("application.validator.year_validator.YearValidator.validate",
                   side_effect=ValueError("Invalid year")):
            scraper = ProcessingScraper()
            with pytest.raises(ValueError, match="Invalid year"):
                scraper.fetch_processing(1900, ProcessingSubOption.subopt_01)

    def test_fetch_processing_returns_empty_list_for_no_data(self):
        mock_soup = MagicMock()

        with patch("adapter.scraper.base_scraper.BaseScraper.fetch_data", return_value=mock_soup), \
                patch("util.utils.Utils.extract_generic_table_data", return_value=[]), \
                patch("application.validator.year_validator.YearValidator.validate", return_value=2023), \
                patch("util.utils.Utils.build_url", return_value=HTTP_FAKE):
            scraper = ProcessingScraper()
            result = scraper.fetch_processing(2023, ProcessingSubOption.subopt_01)

            assert result == []
