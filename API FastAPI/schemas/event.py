from contextlib import nullcontext
from datetime import datetime, timedelta
from typing import Optional, Dict, Union
from pydantic import BaseModel

class EventSchema(BaseModel):
    name: str = ""

    event_host_id: int
    event_datetime: datetime = (datetime.now() + timedelta(hours=1))
    location: str = "No location"
    description: str = "Description"
    icon: str = ""
    max_people: int = 1
    participants: str
    
    config: Dict[str, Union[None, int, bool]] = {"online": False}
