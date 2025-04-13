from unittest.mock import patch, MagicMock

from bs4 import BeautifulSoup

from adapter.scraper.base_scraper import BaseScraper

HTTP_FAKE = "http://fakeurl.com"


class TestBaseScraper:
    def test_fetch_data_returns_parsed_html_when_status_code_is_200(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><body>Test</body></html>"
        with patch("requests.get", return_value=mock_response):
            result = BaseScraper.fetch_data(HTTP_FAKE)
            assert isinstance(result, BeautifulSoup)
            assert result.body.text == "Test"
