from pydantic import BaseModel
from typing import List


class ScamCheckRequest(BaseModel):
    message: str


class ScamCheckResponse(BaseModel):
    risk_level: str
    scam_type: str
    red_flags: List[str]
    advice: str