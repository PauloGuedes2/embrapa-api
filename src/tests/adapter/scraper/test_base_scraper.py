from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from adapter.scraper.base_scraper import BaseScraper

HTTP_FAKE = "http://fakeurl.com"


class TestBaseScraper:
    @patch("adapter.scraper.base_scraper.Utils.get_cache_file_name", return_value="cache/test_cache.txt")
    @patch("adapter.scraper.base_scraper.Utils.get_cache", return_value=None)
    @patch("builtins.open", create=True)
    @patch("requests.get")
    def test_fetch_data_returns_parsed_html_when_status_code_is_200(
        self, mock_requests_get, mock_open, mock_get_cache, mock_get_cache_file_name
    ):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><body>Test</body></html>"
        mock_requests_get.return_value = mock_response

        result = BaseScraper.fetch_data(HTTP_FAKE)

        assert isinstance(result, BeautifulSoup)
        assert result.body.text == "Test"