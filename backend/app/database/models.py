from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database.database import Base


class Investigation(Base):

    __tablename__ = "investigations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    ioc = Column(
        String,
        nullable=False
    )

    ioc_type = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False
    )

    threat_score = Column(
        Integer
    )

    virustotal_score = Column(
        Integer
    )

    alienvault_score = Column(
        Integer,
        nullable=True
    )

    abuseipdb_score = Column(
        Integer,
        nullable=True
    )

    owasp_category = Column(
        String,
        nullable=True
    )

    mitre_tactics = Column(
        String,
        nullable=True
    )

    investigated_at = Column(
        DateTime,
        default=datetime.utcnow
    )