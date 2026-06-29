from app.database.alert_models import Alert


def save_alert(db, response):

    alert = Alert(

        ioc=response["ioc"],

        ioc_type=response["ioc_type"],

        status=response["status"],

        threat_score=response["threatlens_score"]

    )

    db.add(alert)

    db.commit()

    db.refresh(alert)

    return alert