from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/", include_in_schema=False)
def read_root():
    return JSONResponse(
        content={
            "message": "Embrapa Vitivinicultura API",
            "documentation": "/embrapa-vitivinicultura/docs"
        }
    )