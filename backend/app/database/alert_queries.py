from sqlalchemy.orm import Session

from app.database.alert_models import Alert


def get_all_alerts(db: Session):

    alerts = (

        db.query(Alert)

        .order_by(Alert.created_at.desc())

        .all()

    )

    return alerts