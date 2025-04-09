class CustomException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class YearValidationError(CustomException):
    def __init__(self, year: int, base_url: str, valid_range: tuple[int, int], message: str = None):
        self.year = year
        self.base_url = base_url
        self.valid_range = valid_range

        if message is None:
            min_year, max_year = valid_range
            message = (
                f"Invalid year {year} for URL '{base_url}'. "
                f"Must be between {min_year} and {max_year}."
            )

        super().__init__(message)


class DataFetchError(CustomException):
    def __init__(self, url: str, message: str = "Error fetching data from URL."):
        self.url = url
        self.message = message
        super().__init__(self.message)


class NotFoundError(CustomException):
    def __init__(self, resource: str, message: str = "Resource not found."):
        self.resource = resource
        self.message = message
        super().__init__(self.message)
