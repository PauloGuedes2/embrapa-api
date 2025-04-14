import pytest

from exceptions.custom_exceptions import CustomException, YearValidationError, DataFetchError, NotFoundError


class TestCustomExceptions:
    def test_custom_exception_with_message(self):
        exc = CustomException("Erro customizado")
        assert str(exc) == "Erro customizado"
        assert exc.message == "Erro customizado"

    def test_custom_exception_without_message_raises_error(self):
        with pytest.raises(TypeError):
            CustomException()

    def test_year_validation_error_with_custom_message(self):
        exc = YearValidationError(
            year=2025,
            base_url="/api/data",
            valid_range=(1970, 2023),
            message="Ano inválido específico"
        )
        assert str(exc) == "Ano inválido específico"
        assert exc.year == 2025
        assert exc.base_url == "/api/data"
        assert exc.valid_range == (1970, 2023)

    def test_year_validation_error_with_default_message(self):
        exc = YearValidationError(
            year=2025,
            base_url="/api/special",
            valid_range=(1970, 2023)
        )
        expected_msg = "Invalid year 2025 for URL '/api/special'. Must be between 1970 and 2023."
        assert str(exc) == expected_msg

    def test_year_validation_error_attributes(self):
        exc = YearValidationError(
            year=1999,
            base_url="/api/old",
            valid_range=(2000, 2023)
        )
        assert exc.year == 1999
        assert exc.base_url == "/api/old"
        assert exc.valid_range == (2000, 2023)

    def test_data_fetch_error_default_message(self):
        exc = DataFetchError(url="/api/data")
        assert str(exc) == "Error fetching data from URL."
        assert exc.url == "/api/data"

    def test_data_fetch_error_custom_message(self):
        exc = DataFetchError(url="/api/data", message="Connection failed")
        assert str(exc) == "Connection failed"
        assert exc.url == "/api/data"

    def test_not_found_error_default_message(self):
        exc = NotFoundError(resource="abc")
        assert str(exc) == "Resource not found."
        assert exc.resource == "abc"

    def test_not_found_error_custom_message(self):
        exc = NotFoundError(resource="user#", message="user not found")
        assert str(exc) == "user not found"
        assert exc.resource == "user#"

    def test_not_found_error_with_resource_in_message(self):
        message = "resource user# must be not found"
        exc = NotFoundError(resource="user#", message=message)
        assert str(exc) == "resource user# must be not found"
