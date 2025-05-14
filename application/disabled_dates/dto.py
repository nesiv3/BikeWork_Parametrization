from pydantic import BaseModel
from datetime import date, datetime

class DisabledDateDTO(BaseModel):
    id: int
    the_date: date
    reason: str
    created_at: datetime | None = None

    class Config:
        from_attributes = True