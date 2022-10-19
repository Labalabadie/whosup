from socket import AI_NUMERICHOST
from typing import Any, Union
from datetime import datetime
from pydantic import BaseModel as pyBaseModel

class UserSchema(pyBaseModel):
    id: int
    name: str = ""
    email: str = ""
    password: str = ""
    phone: str = ""
    created_at: Any
    updated_at: Any


class UserSchemaDetail(pyBaseModel):
    id: int
    name: str = ""
    email: str = ""
    password: str = ""
    phone: str = ""
    created_at: Any
    updated_at: Any
    hosted_events: Any
    admin_groups: Any
    admin_channels: Any
    contacts: Any
    in_contacts_of: Any


