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
                f"Ano inválido {year} para a URL '{base_url}'. "
                f"Deve estar entre {min_year} e {max_year}."
            )

        super().__init__(message)


class DataFetchError(CustomException):
    def __init__(self, url: str, message: str = "Erro ao buscar dados da URL."):
        self.url = url
        self.message = message
        super().__init__(self.message)


class NotFoundError(CustomException):
    def __init__(self, resource: str, message: str = "Recurso não encontrado."):
        self.resource = resource
        self.message = message
        super().__init__(self.message)


class AuthError(CustomException):
    def __init__(self, message: str = "Falha na autenticação"):
        super().__init__(message)


class InvalidTokenError(AuthError):
    def __init__(self, message: str = "Token inválido"):
        super().__init__(message)


class ExpiredTokenError(AuthError):
    def __init__(self, message: str = "Token expirado"):
        super().__init__(message)


class PermissionDeniedError(AuthError):
    def __init__(self, message: str = "Permissão negada"):
        super().__init__(message)