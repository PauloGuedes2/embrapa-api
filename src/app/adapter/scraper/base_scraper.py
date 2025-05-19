import requests
from typing import Optional
from util.utils import Utils
from bs4 import BeautifulSoup
from config.logger import logger
from abc import ABC, abstractmethod
from domain.entities.export_entity import ExportEntity
from domain.entities.import_entity import ImportEntity
from exceptions.custom_exceptions import DataFetchError
from domain.entities.processing_entity import ProcessingEntity
from domain.entities.production_entity import ProductionEntity
from domain.entities.commercialization_entity import CommercializationEntity
from domain.enum.enums import ExportSubOption, ImportSubOption, ProcessingSubOption


class BaseScraper(ABC):
    def __init__(self, base_url: str):
        self.base_url = base_url

    @staticmethod
    def fetch_data(url) -> BeautifulSoup:
        cache_file_name = Utils.get_cache_file_name(url)
        cache = Utils.get_cache(cache_file_name)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(cache_file_name, 'w', encoding='utf-8') as file:
                    file.write(response.text)
                return BeautifulSoup(response.text, "html.parser")
            logger.error(f"Falha ao buscar dados. Status code: {response.status_code}, URL: {url}")
            raise DataFetchError(url)
        except Exception as e:
            if cache:
                return cache
            raise e

class ProductionScraperBase(BaseScraper):
    @abstractmethod
    def fetch_production(self, year: Optional[int]) -> list[ProductionEntity]:
        pass


class CommercializationScraperBase(BaseScraper):
    @abstractmethod
    def fetch_commercialization(self, year: Optional[int]) -> list[CommercializationEntity]:
        pass


class ImportScraperBase(BaseScraper):
    @abstractmethod
    def fetch_import(self, year: Optional[int], sub_option: Optional[ImportSubOption]) -> list[ImportEntity]:
        pass


class ExportScraperBase(BaseScraper):
    @abstractmethod
    def fetch_export(self, year: Optional[int], sub_option: Optional[ExportSubOption]) -> list[ExportEntity]:
        pass


class ProcessingScraperBase(BaseScraper):
    @abstractmethod
    def fetch_processing(self, year: Optional[int], sub_option: Optional[ProcessingSubOption]) -> list[ProcessingEntity]:
        pass
