class CustomException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class YearValidationError(CustomException):
    def __init__(self, year: int, message: str = "Year must be between 1970 and 2023."):
        self.year = year
        self.message = message
        super().__init__(self.message)

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