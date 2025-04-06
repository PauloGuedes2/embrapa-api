from typing import Optional

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
