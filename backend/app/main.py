from fastapi import FastAPI

from app.api.investigation import router as investigation_router

app = FastAPI(
    title="ThreatLens AI",
    version="1.0.0"
)

app.include_router(investigation_router)


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