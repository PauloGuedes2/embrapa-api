from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
from exceptions.custom_exceptions import DataFetchError


class BaseScraper(ABC):
    def __init__(self, base_url: str):
        self.base_url = base_url

    @staticmethod
    def fetch_data(url) -> BeautifulSoup:
        response = requests.get(url)
        if response.status_code != 200:
            raise DataFetchError(url)
        return BeautifulSoup(response.text, "html.parser")


class ProductionScraperBase(BaseScraper):
    @abstractmethod
    def fetch_production(self, year: int) -> list:
        pass


class CommercializationScraperBase(BaseScraper):
    @abstractmethod
    def fetch_commercialization(self, year: int) -> list:
        pass