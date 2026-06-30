from fastapi import APIRouter

from app.database.database import SessionLocal
from app.database.dashboard import get_dashboard_statistics

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    db = SessionLocal()

    try:

        statistics = get_dashboard_statistics(db)

        return statistics

    finally:

        db.close()