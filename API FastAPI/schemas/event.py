import datetime
import json
from typing import Optional
from pydantic import BaseModel

class EventSchema(BaseModel):
    id: Optional[str]
    name: str
    event_host: str
    event_datetime: datetime
    location: str
    description: str
    icon: str
    max_people: int
    participants: str
    config: json
