from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class EventSchema(BaseModel):
    id: Optional[str]
    name: str

    event_host: int
    event_datetime: datetime
    location: str
    description: str
    icon: str
    max_people: int
    participants: str
    
    config: dict = None
 