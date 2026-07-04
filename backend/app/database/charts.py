from sqlalchemy import func
from app.database.models import Investigation


def get_chart_statistics(db):

    safe = db.query(Investigation).filter(
        Investigation.status == "Safe"
    ).count()

    suspicious = db.query(Investigation).filter(
        Investigation.status == "Suspicious"
    ).count()

    malicious = db.query(Investigation).filter(
        Investigation.status == "Malicious"
    ).count()

    ioc_distribution = (
        db.query(
            Investigation.ioc_type,
            func.count(Investigation.id)
        )
        .group_by(Investigation.ioc_type)
        .all()
    )

    return {

        "threat_distribution": {
            "safe": safe,
            "suspicious": suspicious,
            "malicious": malicious
        },

        "ioc_distribution": [

            {
                "type": row[0],
                "count": row[1]
            }

            for row in ioc_distribution

        ]

    }