from typing import Optional
from pydantic import BaseModel

class GroupSchema(BaseModel):
    id: int = ""
    name: str = ""
    group_admin_id: int = ""
    description: str = ""

class GroupSchemaDetail(pyBaseModel):
    group_admin_name: str = ""
    group_admin_id: int = ""
    created_at: Any
    updated_at: Any
    joined_events: Any
    contacts: Any
    in_contacts_of: Any
