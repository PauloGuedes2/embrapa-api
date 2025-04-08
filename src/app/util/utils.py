from typing import Optional, Callable, List, Any

from bs4 import BeautifulSoup

from exceptions.custom_exceptions import YearValidationError


class Utils:
    @staticmethod
    def validate_year(year: Optional[int] = None) -> Optional[int]:
        if year is None:
            return None

        if not isinstance(year, int):
            raise ValueError("Year must be an integer.")

        if not 1970 <= year <= 2023:
            raise YearValidationError(year)

        return year

    @staticmethod
    def extract_generic_table_data(
            soup: BeautifulSoup,
            table_class: str,
            skip_rows: int,
            transformer: Optional[Callable[[List[str]], Any]] = None
    ) -> List[List[str]]:
        """
        Generic table extractor that can handle different table structures.

        Args:
            soup: BeautifulSoup object
            table_class: CSS class of the table
            skip_rows: Number of header rows to skip
            transformer: Optional function to transform row data

        Returns:
            List of rows, each row being a list of cell values (already stripped)
        """
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
