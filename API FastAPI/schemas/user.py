from typing import Any
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
    created_at: datetime | str
    updated_at: datetime | str
    hosted_events: Any

