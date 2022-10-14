from typing import Optional
from pydantic import BaseModel

class GroupSchema(BaseModel):
    name: str = ""
    admin: int = ""
    description: str = ""