from unittest.mock import patch, MagicMock

import pytest

from src.app.adapter.scraper.production_scraper import ProductionScraper

HTTP_FAKE = "http://fakeurl.com"


class TestProductionScraper:
    def test_fetch_production_returns_entities_for_valid_year(self):
        mock_soup = MagicMock()
        mock_table_data = [["Product A", "100"], ["Product B", "200"]]
        with patch("adapter.scraper.base_scraper.BaseScraper.fetch_data", return_value=mock_soup), \
                patch("util.utils.Utils.extract_generic_table_data", return_value=mock_table_data), \
                patch("application.validator.year_validator.YearValidator.validate", return_value=2023), \
                patch("util.utils.Utils.build_url", return_value=HTTP_FAKE):
            scraper = ProductionScraper()
            result = scraper.fetch_production(2023)
            assert len(result) == 2
            assert result[0].product == "Product A"
            assert result[0].quantity == "100"
            assert result[1].product == "Product B"
            assert result[1].quantity == "200"

    def test_fetch_production_raises_error_for_invalid_year(self):
        with patch("application.validator.year_validator.YearValidator.validate",
                   side_effect=ValueError("Invalid year")):
            scraper = ProductionScraper()
            with pytest.raises(ValueError, match="Invalid year"):
                scraper.fetch_production(1900)

    def test_fetch_production_returns_empty_list_for_no_data(self):
        mock_soup = MagicMock()
        with patch("adapter.scraper.base_scraper.BaseScraper.fetch_data", return_value=mock_soup), \
                patch("util.utils.Utils.extract_generic_table_data", return_value=[]), \
                patch("application.validator.year_validator.YearValidator.validate", return_value=2023), \
                patch("util.utils.Utils.build_url", return_value=HTTP_FAKE):
            scraper = ProductionScraper()
            result = scraper.fetch_production(2023)
            assert result == []
