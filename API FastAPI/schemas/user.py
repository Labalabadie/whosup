from typing import Optional
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
