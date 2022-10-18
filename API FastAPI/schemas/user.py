from typing import Any, Union
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
    created_at: Union
    updated_at: Union[str, datetime]
    hosted_events: Union[str, datetime]

