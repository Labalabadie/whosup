from typing import Any, Optional
from pydantic import BaseModel

class ChannelSchema(BaseModel):
    id: int = ""
    created_at: Any
    updated_at: Any

