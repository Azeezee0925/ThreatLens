from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.database import Base


class Alert(Base):

    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    ioc = Column(String)

    ioc_type = Column(String)

    status = Column(String)

    threat_score = Column(Integer)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )