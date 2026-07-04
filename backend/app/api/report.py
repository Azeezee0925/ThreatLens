from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.investigation import InvestigationRequest
from app.services.investigation_service import investigate
from app.services.pdf_service import generate_pdf

router = APIRouter()


@router.post("/report")
def generate_report(request: InvestigationRequest):

    result = investigate(request.ioc)

    pdf = generate_pdf(result)

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="ThreatLens_Report.pdf"'
        },
    )