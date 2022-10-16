from typing import List
from datetime import datetime
from pydantic import BaseModel as pyBaseModel

class UserSchema(pyBaseModel):
    id: int
    name: str = ""
    email: str = ""
    password: str = ""
    phone: str = ""
    created_at: datetime
    updated_at: datetime


class UserSchemaDetail(pyBaseModel):
    id: int
    name: str = ""
    email: str = ""
    password: str = ""
    phone: str = ""
    created_at: datetime
    updated_at: datetime
    hosted_events: List
    attending_events: List
    admin_channels: List
    admin_groups: List
