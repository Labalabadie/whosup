from typing import Any, Optional
from pydantic import BaseModel

class NotificationSchema(BaseModel):
    text: str = ""