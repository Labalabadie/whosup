from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel

class EventSchema(BaseModel):
    name: str

    event_host: int
    event_datetime: datetime = (datetime.now + timedelta(hours=1))
    location: str
    description: str
    icon: str = ""
    max_people: int = 1
    participants: str
    
    config: dict = None
 