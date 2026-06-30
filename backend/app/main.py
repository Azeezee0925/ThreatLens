from fastapi import FastAPI

from app.api.investigation import router as investigation_router
from app.api.history import router as history_router
from app.api.dashboard import router as dashboard_router
from app.database.database import Base, engine
from app.database import models
from app.database.database import Base, engine
from app.database.models import Investigation
from app.database.alert_models import Alert
from app.api import alerts

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ThreatLens AI",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(investigation_router)
app.include_router(history_router)
app.include_router(dashboard_router)
app.include_router(alerts.router)


@app.get("/")
def root():
    return {
        "message": "ThreatLens AI Backend Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }