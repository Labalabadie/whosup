from typing import Optional
from pydantic import BaseModel

class GroupSchema(BaseModel):
    name: str = ""
    group_admin_id: int = ""
    description: str = ""