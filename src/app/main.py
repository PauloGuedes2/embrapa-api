import os

import uvicorn
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

from api.controllers.auth_controller import router as auth_router
from api.controllers.commercialization_controller import router as commercialization_router
from api.controllers.export_controller import router as export_router
from api.controllers.import_controller import router as import_router
from api.controllers.processing_controller import router as processing_router
from api.controllers.production_controller import router as production_router
from api.controllers.root_controller import router as root_router
from config.logger import logger
from config.params import ROUTER_PREFIX
from exceptions.custom_exceptions import YearValidationError, DataFetchError, NotFoundError, AuthError, \
    PermissionDeniedError
from infrastructure.db.init_db import DatabaseInitializer
from infrastructure.docs.openapi_config import custom_openapi

app = FastAPI(
    title="Embrapa API",
    description="API para gerenciamento de dados de produção, processamento, comercialização, importação e exportação da vitivinicultura.",
    version="1.0.0"
)

app.openapi = lambda: custom_openapi(app, token_url=f"{ROUTER_PREFIX}/auth/login")
app.include_router(auth_router, prefix=ROUTER_PREFIX, tags=["Autenticação"])
app.include_router(production_router, prefix=ROUTER_PREFIX, tags=["Produção"])
app.include_router(processing_router, prefix=ROUTER_PREFIX, tags=["Processamento"])
app.include_router(commercialization_router, prefix=ROUTER_PREFIX, tags=["Comercialização"])
app.include_router(import_router, prefix=ROUTER_PREFIX, tags=["Importação"])
app.include_router(export_router, prefix=ROUTER_PREFIX, tags=["Exportação"])
app.include_router(root_router)


@app.exception_handler(YearValidationError)
async def year_validation_exception_handler(request: Request, exc: YearValidationError):
    logger.error(f"Validação de ano falhou: {exc.message} | Ano: {exc.year}")
    return JSONResponse(
        status_code=400,
        content={"mensagem": exc.message, "ano": exc.year},
    )


@app.exception_handler(DataFetchError)
async def data_fetch_error_handler(request: Request, exc: DataFetchError):
    logger.error(f"Erro ao buscar dados: {exc.message} | URL: {exc.url}")
    return JSONResponse(
        status_code=500,
        content={"mensagem": exc.message, "url": exc.url},
    )


@app.exception_handler(NotFoundError)
async def not_found_error_handler(request: Request, exc: NotFoundError):
    logger.error(f"Recurso não encontrado: {exc.message} | Recurso: {exc.resource}")
    return JSONResponse(
        status_code=404,
        content={"mensagem": exc.message, "recurso": exc.resource},
    )


@app.exception_handler(AuthError)
async def auth_error_handler(request: Request, exc: AuthError):
    logger.error(f"Erro de autenticação: {exc.message}")
    return JSONResponse(
        status_code=401,
        content={"mensagem": exc.message},
        headers={"WWW-Authenticate": "Bearer"}
    )


@app.exception_handler(PermissionDeniedError)
async def permission_denied_handler(request: Request, exc: PermissionDeniedError):
    logger.error(f"Permissão negada: {exc.message}")
    return JSONResponse(
        status_code=403,
        content={"mensagem": exc.message}
    )


class App:
    def __init__(self, host: str = "0.0.0.0", port: int = 8000):
        self.host = os.getenv("HOST", host)
        self.port = int(os.getenv("PORT", port))

    def run(self):
        logger.info("Inicializando banco de dados")
        DatabaseInitializer().init_database()
        logger.info(f"Servidor iniciando em {self.host}:{self.port}")
        uvicorn.run(app, host=self.host, port=self.port)


if __name__ == "__main__":
    application = App()
    application.run()
