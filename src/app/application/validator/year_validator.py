from typing import Optional, Tuple

from exceptions.custom_exceptions import YearValidationError


class YearValidator:
    DEFAULT_RANGE = (1970, 2023)
    SPECIAL_RANGE = (1970, 2024)
    SPECIAL_ENDPOINTS = ("opt_05", "opt_06", "opt_03")

    @classmethod
    def validate(cls, base_url: str, year: Optional[int] = None) -> Optional[int]:
        if year is None:
            return None

        if not isinstance(year, int):
            raise TypeError("Year must be an integer value.")

        valid_range = cls._get_year_range(base_url)
        cls._validate_year_in_range(year, base_url, valid_range)

        return year

    @classmethod
    def _get_year_range(cls, base_url: str) -> Tuple[int, int]:
        return (
            cls.SPECIAL_RANGE
            if base_url.endswith(cls.SPECIAL_ENDPOINTS)
            else cls.DEFAULT_RANGE
        )

    @classmethod
    def _validate_year_in_range(
            cls,
            year: int,
            base_url: str,
            valid_range: Tuple[int, int]
    ) -> None:
        min_year, max_year = valid_range
        if not min_year <= year <= max_year:
            raise YearValidationError(
                year=year,
                base_url=base_url,
                valid_range=valid_range,
                message=(
                    f"Year validation failed for {base_url}. "
                    f"Provided year: {year}, "
                    f"Allowed range: {min_year}-{max_year}"
                )
            )
