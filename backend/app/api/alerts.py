from fastapi import APIRouter

from app.database.database import SessionLocal
from app.database.alert_queries import get_all_alerts

router = APIRouter()


@router.get("/alerts")

def alerts():

    db = SessionLocal()

    try:

        return get_all_alerts(db)

    finally:

        db.close()