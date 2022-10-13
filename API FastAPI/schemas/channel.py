from typing import Optional
from pydantic import BaseModel

class ChannelSchema(BaseModel):
    name: str = ""
    admin: int = ""
    description: str = ""
