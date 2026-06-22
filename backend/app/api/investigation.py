from fastapi import APIRouter
from app.schemas.investigation import InvestigationRequest
from app.services.threat_service import investigate_ioc

router = APIRouter()


@router.post("/investigate")
def investigate(request: InvestigationRequest):
    result = investigate_ioc(
        request.ioc,
        request.ioc_type
    )

    return result