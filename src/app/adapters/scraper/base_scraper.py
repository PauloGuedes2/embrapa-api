from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup


class BaseScraper(ABC):
    def __init__(self, base_url: str):
        self.base_url = base_url

    @staticmethod
    def fetch_data(url) -> BeautifulSoup:
        response = requests.get(url)
        return BeautifulSoup(response.text, "html.parser")

    @abstractmethod
    def fetch_production(self, year: int) -> list:
        pass
