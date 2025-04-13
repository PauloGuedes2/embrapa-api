import logging
import os

import uvicorn
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

from api.controllers.commercialization_controller import router as commercialization_router
from api.controllers.export_controller import router as export_router
from api.controllers.import_controller import router as import_router
from api.controllers.processing_controller import router as processing_router
from api.controllers.production_controller import router as production_router
from exceptions.custom_exceptions import YearValidationError, DataFetchError, NotFoundError

app = FastAPI()

# Register routers
app.include_router(commercialization_router, prefix="/api", tags=["Commercialization"])
app.include_router(production_router, prefix="/api", tags=["Production"])
app.include_router(import_router, prefix="/api", tags=["Import"])
app.include_router(export_router, prefix="/api", tags=["Export"])
app.include_router(processing_router, prefix="/api", tags=["Processing"])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.exception_handler(YearValidationError)
async def year_validation_exception_handler(request: Request, exc: YearValidationError):
    return JSONResponse(
        status_code=400,
        content={"message": exc.message, "year": exc.year},
    )


@app.exception_handler(DataFetchError)
async def data_fetch_error_handler(request: Request, exc: DataFetchError):
    return JSONResponse(
        status_code=500,
        content={"message": exc.message, "url": exc.url},
    )


@app.exception_handler(NotFoundError)
async def not_found_error_handler(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": exc.message, "resource": exc.resource},
    )


class App:
    def __init__(self, host: str = "0.0.0.0", port: int = 8000):
        self.host = os.getenv("HOST", host)
        self.port = int(os.getenv("PORT", port))

    def run(self):
        logger.info(f"Starting server at {self.host}:{self.port}")
        uvicorn.run(app, host=self.host, port=self.port)


if __name__ == "__main__":
    application = App()
    application.run()
