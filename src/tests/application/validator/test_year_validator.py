import pytest

from application.validator.year_validator import YearValidator
from exceptions.custom_exceptions import YearValidationError


class TestYearValidator:
    def test_validate_returns_none_for_none_year(self):
        result = YearValidator.validate(base_url="any_url", year=None)
        assert result is None

    def test_validate_returns_year_when_valid(self):
        result = YearValidator.validate(base_url="any_url", year=2020)
        assert result == 2020

    def test_get_year_range_returns_default_for_normal_endpoints(self):
        for endpoint in ["", "opt_01", "opt_02", "opt_04"]:
            result = YearValidator._get_year_range(f"base/{endpoint}")
            assert result == YearValidator.DEFAULT_RANGE

    def test_get_year_range_returns_special_for_special_endpoints(self):
        for endpoint in YearValidator.SPECIAL_ENDPOINTS:
            result = YearValidator._get_year_range(f"base/{endpoint}")
            assert result == YearValidator.SPECIAL_RANGE

    def test_validate_year_in_range_accepts_valid_year(self):
        YearValidator._validate_year_in_range(
            year=2020,
            base_url="any_url",
            valid_range=(1970, 2023)
        )

    def test_validate_with_special_endpoint_uses_special_range(self):
        for endpoint in YearValidator.SPECIAL_ENDPOINTS:
            result = YearValidator.validate(
                base_url=f"base/{endpoint}",
                year=2024
            )
            assert result == 2024

        for endpoint in YearValidator.SPECIAL_ENDPOINTS:
            with pytest.raises(YearValidationError):
                YearValidator.validate(
                    base_url=f"base/{endpoint}",
                    year=2025
                )

    def test_validate_with_normal_endpoint_uses_default_range(self):
        result = YearValidator.validate(
            base_url="base/opt_01",
            year=2023
        )
        assert result == 2023

        with pytest.raises(YearValidationError):
            YearValidator.validate(
                base_url="base/opt_01",
                year=2024
            )

    def test_validate_year_in_range_accepts_boundary_years(self):
        YearValidator._validate_year_in_range(
            year=1970,
            base_url="any_url",
            valid_range=(1970, 2023)
        )

        YearValidator._validate_year_in_range(
            year=2023,
            base_url="any_url",
            valid_range=(1970, 2023)
        )

    def test_validate_handles_empty_base_url(self):
        with pytest.raises(YearValidationError):
            YearValidator.validate(base_url="", year=2025)
