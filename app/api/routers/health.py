from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/service", summary="Health check for main service")
def health_service():
    return {"status": "ok"}

@router.get("/db", summary="Health check for database")
def health_db(db: Session = Depends(deps.get_db)):
    try:
        # Simple query to check DB connection
        db.execute("SELECT 1")
        return {"status": "ok"}
    except Exception:
        return {"status": "error"}
