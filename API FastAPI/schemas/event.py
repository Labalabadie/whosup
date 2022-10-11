from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class EventSchema(BaseModel):
    name: str

    event_host: int
    event_datetime: datetime
    location: str
    description: str
    icon: str
    max_people: int = 1
    participants: str
    
    config: dict = None
 