from typing import Optional
from datetime import datetime
from pydantic import BaseModel as pyBaseModel

class UserSchema(pyBaseModel):
    name: str = ""
    email: str = ""
    password: str = ""
    phone: str = ""


class UserSchemaDetail(UserSchema):
    id: int
    created_at: datetime
    updated_at: datetime