from sqlalchemy.orm import Session

from app.database.models import Investigation


def save_investigation(db: Session, data: dict):

    investigation = Investigation(

        ioc=data["ioc"],

        ioc_type=data["ioc_type"],

        status=data["status"],

        threat_score=data["threatlens_score"],

        virustotal_score=data["virustotal_score"],

        alienvault_score=data.get("alienvault_score"),

        abuseipdb_score=data.get("abuse_confidence_score"),

        owasp_category=(
            ", ".join(data["owasp_category"])
            if data.get("owasp_category")
            else None
        ),

        mitre_tactics=(
            ", ".join(data["mitre_tactics"])
            if data.get("mitre_tactics")
            else None
        )

    )

    db.add(investigation)

    db.commit()

    db.refresh(investigation)

    return investigation