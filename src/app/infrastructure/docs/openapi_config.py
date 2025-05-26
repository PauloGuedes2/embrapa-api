from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def custom_openapi(app: FastAPI, token_url: str) -> dict:
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Embrapa Vitivinicultura API",
        version="1.0.0",
        description="**API RESTful** moderna, desenvolvida em **Python 3.11 + FastAPI**, cujo objetivo é facilitar o acesso aos dados públicos da vitivinicultura brasileira disponíveis no site da [Embrapa Vitibrasil](http://vitibrasil.cnpuv.embrapa.br/). Esses dados, originalmente apresentados como tabelas em páginas HTML, são extraídos via **web scraping** e organizados para fácil consumo por sistemas e usuários técnicos.\n"
                    "\n"
                    "A API segue princípios da **Clean Architecture**, garantindo organização e escalabilidade. Os dados disponíveis abrangem informações sobre:\n"
                    "\n"
                    "- **Produção**\n"
                    "- **Processamento**\n"
                    "- **Importação**\n"
                    "- **Exportação**\n"
                    "- **Comercialização**\n"
                    "\n"
                    "**Autenticação:** As rotas de dados requerem autenticação via **JWT (Bearer Token)**. Registre um usuário, faça login para obter o token e utilize-o no cabeçalho das requisições protegidas.\n"
                    "\n"
                    "**Status da API:** Utilize a rota `/health` para verificar o status de funcionamento do serviço.",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", []).append({"bearerAuth": []})

    app.openapi_schema = openapi_schema
    return app.openapi_schema
