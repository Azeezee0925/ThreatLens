from fastapi import APIRouter
from app.schemas.investigation import InvestigationRequest

router = APIRouter()


@router.post("/investigate")
def investigate(request: InvestigationRequest):
    return {
        "message": "Investigation request received",
        "ioc": request.ioc,
        "ioc_type": request.ioc_type
    }