from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health", include_in_schema=False)
def health_check():
    return {"status": "healthy"}

@router.api_route("/", methods=["GET", "HEAD"], include_in_schema=False)
def read_root():
    return JSONResponse(
        content={
            "message": "Embrapa Vitivinicultura API",
            "documentation": "/embrapa-vitivinicultura/docs"
        }
    )