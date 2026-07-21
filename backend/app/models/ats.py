from pydantic import BaseModel

class ATSResult(BaseModel):
    matched_skills: list[str]
    missing_skills: list[str]
    match_percentage: float