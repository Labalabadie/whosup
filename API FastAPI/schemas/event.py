from typing import Optional
from pydantic import BaseModel

class Event(BaseModel):
    id: Optional[str]
    event_name: str
    event_datetime: str
    location: str
    description: str
    participants: str
    event_status: str
    nonolist: str