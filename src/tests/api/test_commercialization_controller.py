# import pytest
# from fastapi.testclient import TestClient
# from unittest.mock import MagicMock, patch
# from api.controllers.commercialization_controller import router
# from domain.ports.commercialization_port import CommercializationInterface
#
# client = TestClient(router)
#
#
# class TestCommercializationController:
#     @patch("api.dependencies.scraper_dependencies.ScraperDependencies.get_commercialization_scraper")
#     def test_get_commercialization_returns_data_for_valid_year(self, mock_get_scraper):
#         # Mockando a dependência do scraper
#         scraper_mock = MagicMock(spec=CommercializationInterface)
#         scraper_mock.fetch_commercialization.return_value = [
#             {"product": "VINHO DE MESA", "quantity": "187.016.848"},
#             {"product": "Tinto", "quantity": "165.097.539"},
#             {"product": "Rosado", "quantity": "2.520.748"},
#             {"product": "Branco", "quantity": "19.398.561"},
#         ]
#         mock_get_scraper.return_value = scraper_mock
#
#         # Mockando o endpoint
#         with patch("api.controllers.commercialization_controller.CommercializationController.get_commercialization") as mock_endpoint:
#             mock_endpoint.return_value = scraper_mock.fetch_commercialization(2023)
#             response = client.get("/comercializacao/2023")
#
#         # Verificando a resposta
#         assert response.status_code == 200
#         assert response.json() == [
#             {"product": "VINHO DE MESA", "quantity": "187.016.848"},
#             {"product": "Tinto", "quantity": "165.097.539"},
#             {"product": "Rosado", "quantity": "2.520.748"},
#             {"product": "Branco", "quantity": "19.398.561"},
#         ]
#
#     @patch("api.dependencies.scraper_dependencies.ScraperDependencies.get_commercialization_scraper")
#     def test_get_commercialization_returns_404_for_invalid_year(self, mock_get_scraper):
#         # Mockando a dependência do scraper
#         scraper_mock = MagicMock(spec=CommercializationInterface)
#         scraper_mock.fetch_commercialization.side_effect = ValueError("Invalid year")
#         mock_get_scraper.return_value = scraper_mock
#
#         # Mockando o endpoint
#         with patch("api.controllers.commercialization_controller.CommercializationController.get_commercialization") as mock_endpoint:
#             mock_endpoint.side_effect = ValueError("Invalid year")
#             response = client.get("/comercializacao/1969")
#
#         # Verificando a resposta
#         assert response.status_code == 404
#         assert response.json() == {"detail": "Invalid year"}
#
#     def test_get_commercialization_returns_422_for_missing_year(self):
#         # Mockando o endpoint
#         with patch("api.controllers.commercialization_controller.CommercializationController.get_commercialization") as mock_endpoint:
#             mock_endpoint.return_value = None
#             response = client.get("/comercializacao/")
#
#         # Verificando a resposta
#         assert response.status_code == 422
#         assert "detail" in response.json()