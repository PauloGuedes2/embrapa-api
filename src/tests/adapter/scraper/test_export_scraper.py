from unittest.mock import patch, MagicMock

import pytest

from adapter.scraper.export_scraper import ExportScraper
from domain.enum.enums import ExportSubOption

HTTP_FAKE = "http://fakeurl.com"


class TestExportScraper:
    def test_fetch_export_returns_entities_for_valid_year_and_sub_option(self):
        mock_soup = MagicMock()
        mock_table_data = [["Country A", "1000", "5000"], ["Country B", "2000", "10000"]]
        with patch("adapter.scraper.base_scraper.BaseScraper.fetch_data", return_value=mock_soup), \
                patch("util.utils.Utils.extract_generic_table_data", return_value=mock_table_data), \
                patch("application.validator.year_validator.YearValidator.validate", return_value=2021), \
                patch("util.utils.Utils.build_url", return_value=HTTP_FAKE):
            scraper = ExportScraper()
            result = scraper.fetch_export(2021, ExportSubOption.subopt_01)
            assert len(result) == 2
            assert result[0].country == "Country A"
            assert result[0].quantity == "1000"
            assert result[0].value == "5000"
            assert result[1].country == "Country B"
            assert result[1].quantity == "2000"
            assert result[1].value == "10000"

    def test_fetch_export_raises_error_for_invalid_year(self):
        with patch("application.validator.year_validator.YearValidator.validate",
                   side_effect=ValueError("Invalid year")):
            scraper = ExportScraper()
            with pytest.raises(ValueError, match="Invalid year"):
                scraper.fetch_export(1900, ExportSubOption.subopt_01)

    def test_fetch_export_returns_empty_list_for_no_data(self):
        mock_soup = MagicMock()
        with patch("adapter.scraper.base_scraper.BaseScraper.fetch_data", return_value=mock_soup), \
                patch("util.utils.Utils.extract_generic_table_data", return_value=[]), \
                patch("application.validator.year_validator.YearValidator.validate", return_value=2023), \
                patch("util.utils.Utils.build_url", return_value=HTTP_FAKE):
            scraper = ExportScraper()
            result = scraper.fetch_export(2023, ExportSubOption.subopt_01)
            assert result == []
