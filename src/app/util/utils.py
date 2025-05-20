import os
from bs4 import BeautifulSoup
from config.logger import logger
from urllib.parse import urlparse, parse_qs
from datetime import datetime, timezone, timedelta
from typing import Optional, Callable, List, Any, Union
from domain.enum.enums import ImportSubOption, ExportSubOption, ProcessingSubOption


class Utils:
    @staticmethod
    def extract_generic_table_data(
            soup: BeautifulSoup,
            table_class: str,
            skip_rows: int,
            transformer: Optional[Callable[[List[str]], Any]] = None
    ) -> List[List[str]]:

        table = soup.find("table", {"class": table_class})
        if not table:
            logger.error(f"Tabela não encontrada com a classe: {table_class}")
            raise ValueError

        data = []
        for row in table.find_all("tr")[skip_rows:]:
            cols = [col.text.strip() for col in row.find_all("td")]
            if transformer:
                cols = transformer(cols)
            if cols:
                data.append(cols)

        return data

    @staticmethod
    def build_url(
            base_url: str,
            year: Optional[int] = None,
            sub_option: Optional[Union[ImportSubOption, ExportSubOption, ProcessingSubOption]] = None,
            year_query_param: str = "ano",
            suboption_query_param: str = "subopcao"
    ) -> str:

        if sub_option:
            if "opcao=opt_05" in base_url and not isinstance(sub_option, ImportSubOption):
                logger.error("Tipo de subopção inválida para URL de importação")
                raise ValueError
            if "opcao=opt_06" in base_url and not isinstance(sub_option, ExportSubOption):
                logger.error("Tipo de subopção inválida para URL de exportação")
                raise ValueError
            if "opcao=opt_03" in base_url and not isinstance(sub_option, ProcessingSubOption):
                logger.error("Tipo de subopção inválida para URL de processamento")
                raise ValueError

        params = []
        if year is not None:
            params.append(f"{year_query_param}={year}")
        if sub_option is not None:
            params.append(f"{suboption_query_param}={sub_option.name}")

        if not params:
            return base_url

        return f"{base_url}{'&' if '?' in base_url else '?'}{'&'.join(params)}"

    @staticmethod
    def get_current_utc_brasilia():
        return datetime.now(timezone.utc) + timedelta(hours=-3)

    @staticmethod
    def get_cache(file):
        try:
            with open(file, 'r', encoding='utf-8') as arquivo:
                return BeautifulSoup(arquivo.read(), "html.parser")
        except FileNotFoundError:
            return None

    @staticmethod
    def get_cache_file_name(url):
        query_params = parse_qs(urlparse(url).query)
        option = query_params.get('opcao', ['NA'])[0]
        year = query_params.get('ano', ['NA'])[0]
        suboption = query_params.get('subopcao', ['NA'])[0]
        base_dir = os.path.abspath(os.path.dirname(__file__))
        cache_dir = os.path.abspath(os.path.join(base_dir, '..', 'cache'))
        return os.path.join(cache_dir, f'{option}_{year}_{suboption}.txt')