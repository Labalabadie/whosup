from typing import Optional
from pydantic import BaseModel

class ChannelSchema(BaseModel):
    name: str = ""
    channel_admin_id: int = ""
    description: str = ""
