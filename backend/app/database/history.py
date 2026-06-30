from sqlalchemy.orm import Session

from app.database.models import Investigation


def get_all_investigations(db: Session):

    return (

        db.query(Investigation)

        .order_by(Investigation.investigated_at.desc())

        .all()

    )