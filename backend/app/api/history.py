from fastapi import APIRouter

from app.database.database import SessionLocal
from app.database.history import get_all_investigations

router = APIRouter()


@router.get("/history")
def history():

    db = SessionLocal()

    try:

        investigations = get_all_investigations(db)

        return investigations

    finally:

        db.close()