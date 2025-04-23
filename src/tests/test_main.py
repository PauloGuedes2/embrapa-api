import json
from unittest.mock import patch, MagicMock

import pytest
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from config.params import ROUTER_PREFIX
from exceptions.custom_exceptions import YearValidationError, DataFetchError, NotFoundError
from main import app, App


class TestMain:
    @pytest.fixture
    def mock_uvicorn(self):
        with patch('main.uvicorn.run') as mock:
            yield mock

    @pytest.fixture
    def mock_logger(self):
        with patch('main.logger.info') as mock:
            yield mock

    def test_app_config(self):
        assert isinstance(app, FastAPI)
        assert len(app.routes) > 0

    def test_routers_registered(self):
        paths = {str(route.path) for route in app.routes}
        expected_paths = {
            f"{ROUTER_PREFIX}/producao/{{ano}}",
            f"{ROUTER_PREFIX}/processamento/{{ano}}/{{subopcao}}",
            f"{ROUTER_PREFIX}/comercializacao/{{ano}}",
            f"{ROUTER_PREFIX}/importacao/{{ano}}/{{subopcao}}",
            f"{ROUTER_PREFIX}/exportacao/{{ano}}/{{subopcao}}"
        }
        assert expected_paths.issubset(paths)

    def test_exception_handlers_registered(self):
        handlers = app.exception_handlers
        assert YearValidationError in handlers
        assert DataFetchError in handlers
        assert NotFoundError in handlers

    def test_app_run_default(self, mock_uvicorn, mock_logger):
        App().run()
        mock_logger.assert_called_once_with("Starting server at 0.0.0.0:8000")
        mock_uvicorn.assert_called_once_with(app, host="0.0.0.0", port=8000)

    def test_app_run_with_env(self, mock_uvicorn):
        with patch.dict('os.environ', {'HOST': 'localhost', 'PORT': '8080'}):
            App().run()
        mock_uvicorn.assert_called_once_with(app, host="localhost", port=8080)

    def test_app_run_custom(self, mock_uvicorn):
        App(host="127.0.0.1", port=5000).run()
        mock_uvicorn.assert_called_once_with(app, host="127.0.0.1", port=5000)

    def test_app_port_conversion_error(self):
        with patch.dict('os.environ', {'PORT': 'invalid'}):
            with pytest.raises(ValueError):
                App()

    @pytest.mark.asyncio
    async def test_year_validation_exception_handler(self):
        request = MagicMock(spec=Request)
        exc = YearValidationError(
            message="Ano inválido",
            year=1800,
            base_url="http://example.com",
            valid_range=(2000, 2023)
        )
        response = await app.exception_handlers[YearValidationError](request, exc)
        assert isinstance(response, JSONResponse)
        assert response.status_code == 400
        assert json.loads(response.body) == {"message": "Ano inválido", "year": 1800}

    @pytest.mark.asyncio
    async def test_data_fetch_error_handler(self):
        request = MagicMock(spec=Request)
        exc = DataFetchError(message="Erro ao buscar dados", url="http://fake-url")
        response = await app.exception_handlers[DataFetchError](request, exc)
        assert isinstance(response, JSONResponse)
        assert response.status_code == 500
        assert json.loads(response.body) == {"message": "Erro ao buscar dados", "url": "http://fake-url"}

    @pytest.mark.asyncio
    async def test_not_found_error_handler(self):
        request = MagicMock(spec=Request)
        exc = NotFoundError(message="Recurso não encontrado", resource="relatorio.csv")
        response = await app.exception_handlers[NotFoundError](request, exc)
        assert isinstance(response, JSONResponse)
        assert response.status_code == 404
        assert json.loads(response.body) == {"message": "Recurso não encontrado", "resource": "relatorio.csv"}
