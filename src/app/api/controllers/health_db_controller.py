from fastapi import APIRouter, Depends
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text
from infrastructure.db.session import get_db

router = APIRouter()

@router.get("/healthdb")
def health_check(db = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except OperationalError:
        return {"status": "degraded", "database": "unreachable"}