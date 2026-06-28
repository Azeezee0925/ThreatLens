from pydantic import BaseModel


class InvestigationRequest(BaseModel):
    ioc: str