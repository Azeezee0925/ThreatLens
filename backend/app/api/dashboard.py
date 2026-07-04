from fastapi import APIRouter

from app.database.database import SessionLocal
from app.database.dashboard import get_dashboard_statistics
from app.database.charts import get_chart_statistics
from app.database.trends import get_weekly_trend

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    db = SessionLocal()

    try:
        return get_dashboard_statistics(db)

    finally:
        db.close()


@router.get("/dashboard/charts")
def dashboard_charts():

    db = SessionLocal()

    try:

        chart_data = get_chart_statistics(db)

        chart_data["weekly_trend"] = get_weekly_trend(db)

        return chart_data

    finally:
        db.close()