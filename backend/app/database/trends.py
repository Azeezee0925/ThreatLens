from datetime import datetime, timedelta
from sqlalchemy import func

from app.database.models import Investigation


def get_weekly_trend(db):

    today = datetime.utcnow().date()

    trend = []

    for i in range(6, -1, -1):

        day = today - timedelta(days=i)

        count = db.query(
            func.count(Investigation.id)
        ).filter(
            func.date(Investigation.investigated_at) == day
        ).scalar()

        trend.append({
            "day": day.strftime("%a"),
            "count": count
        })

    return trend