from fastapi import APIRouter

from app.schemas.investigation import InvestigationRequest

from app.services.investigation_service import investigate as investigate_service

router = APIRouter()


@router.post("/investigate")
def investigate(request: InvestigationRequest):

    result = investigate_service(request.ioc)

    return result