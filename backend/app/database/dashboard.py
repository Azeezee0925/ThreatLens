from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.models import Investigation


def get_dashboard_statistics(db: Session):

    total = db.query(Investigation).count()

    safe = db.query(Investigation).filter(
        Investigation.status == "Safe"
    ).count()

    low_risk = db.query(Investigation).filter(
        Investigation.status == "Low Risk"
    ).count()

    suspicious = db.query(Investigation).filter(
        Investigation.status == "Suspicious"
    ).count()

    malicious = db.query(Investigation).filter(
        Investigation.status == "Malicious"
    ).count()

    ip_count = db.query(Investigation).filter(
        Investigation.ioc_type == "ip"
    ).count()

    domain_count = db.query(Investigation).filter(
        Investigation.ioc_type == "domain"
    ).count()

    url_count = db.query(Investigation).filter(
        Investigation.ioc_type == "url"
    ).count()

    hash_count = db.query(Investigation).filter(
        Investigation.ioc_type.in_(
            ["md5", "sha1", "sha256"]
        )
    ).count()

    average_score = db.query(
        func.avg(
            Investigation.threat_score
        )
    ).scalar()

    highest_score = db.query(
        func.max(
            Investigation.threat_score
        )
    ).scalar()

    latest = (

        db.query(Investigation)

        .order_by(
            Investigation.investigated_at.desc()
        )

        .first()

    )

    return {

        "total_investigations": total,

        "safe": safe,

        "low_risk": low_risk,

        "suspicious": suspicious,

        "malicious": malicious,

        "ip_count": ip_count,

        "domain_count": domain_count,

        "url_count": url_count,

        "hash_count": hash_count,

        "average_threat_score": round(
            average_score or 0,
            2
        ),

        "highest_threat_score": highest_score or 0,

        "latest_investigation": (
            latest.investigated_at
            if latest
            else None
        )

    }