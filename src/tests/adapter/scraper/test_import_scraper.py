from unittest.mock import patch, MagicMock

import pytest

from adapter.scraper.import_scraper import ImportScraper
from domain.enum.enums import ImportSubOption

HTTP_FAKE = "http://fakeurl.com"


class TestImportScraper:
    def test_fetch_import_returns_entities_for_valid_year_and_suboption(self):
        mock_soup = MagicMock()
        mock_table_data = [["Country A", "500", "2500"], ["Country B", "1000", "5000"]]
        with patch("adapter.scraper.base_scraper.BaseScraper.fetch_data", return_value=mock_soup), \
                patch("util.utils.Utils.extract_generic_table_data", return_value=mock_table_data), \
                patch("application.validator.year_validator.YearValidator.validate", return_value=2023), \
                patch("util.utils.Utils.build_url", return_value=HTTP_FAKE):
            scraper = ImportScraper()
            result = scraper.fetch_import(2023, ImportSubOption.subopt_02)
            assert len(result) == 2
            assert result[0].country == "Country A"
            assert result[0].quantity == "500"
            assert result[0].value == "2500"
            assert result[1].country == "Country B"
            assert result[1].quantity == "1000"
            assert result[1].value == "5000"

    def test_fetch_import_raises_error_for_invalid_year(self):
        with patch("application.validator.year_validator.YearValidator.validate",
                   side_effect=ValueError("Invalid year")):
            scraper = ImportScraper()
            with pytest.raises(ValueError, match="Invalid year"):
                scraper.fetch_import(1900, ImportSubOption.subopt_02)

    def test_fetch_import_returns_empty_list_for_no_data(self):
        mock_soup = MagicMock()
        with patch("adapter.scraper.base_scraper.BaseScraper.fetch_data", return_value=mock_soup), \
                patch("util.utils.Utils.extract_generic_table_data", return_value=[]), \
                patch("application.validator.year_validator.YearValidator.validate", return_value=2023), \
                patch("util.utils.Utils.build_url", return_value=HTTP_FAKE):
            scraper = ImportScraper()
            result = scraper.fetch_import(2023, ImportSubOption.subopt_02)
            assert result == []
