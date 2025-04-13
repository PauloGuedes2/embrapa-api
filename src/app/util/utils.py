from typing import Optional, Callable, List, Any, Union

from bs4 import BeautifulSoup

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
            raise ValueError(f"Table with class '{table_class}' not found")

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
                raise ValueError("URL de importação requer ImportSubOption")
            if "opcao=opt_06" in base_url and not isinstance(sub_option, ExportSubOption):
                raise ValueError("URL de exportação requer ExportSubOption")
            if "opcao=opt_03" in base_url and not isinstance(sub_option, ProcessingSubOption):
                raise ValueError("URL de processamento requer ProcessingSubOption")

        params = []
        if year is not None:
            params.append(f"{year_query_param}={year}")
        if sub_option is not None:
            params.append(f"{suboption_query_param}={sub_option.name}")

        if not params:
            return base_url

        return f"{base_url}{'&' if '?' in base_url else '?'}{'&'.join(params)}"
