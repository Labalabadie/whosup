from contextlib import nullcontext
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Union
from pydantic import BaseModel

class EventSchema(BaseModel):
    name: str = "Event name"

    event_host_id: int
    event_datetime: datetime = (datetime.now() + timedelta(hours=1))
    location: str = "Location"
    description: str = "Description"
    icon: str = ""
    max_people: int = 1
    participants: List[int] = []
    
    config: Dict[str, Union[None, int, bool]] = {
        "online": False, 
        "group_id": 0, # None for no group
        "channel_id": 0 # None for no channel
    }