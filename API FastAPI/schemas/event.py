<<<<<<< HEAD
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
=======
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
>>>>>>> 2f9ef4324d3b07ca3809107279c7e760baae2a72
    nonolist: str