from typing import Optional
from pydantic import BaseModel as pyBaseModel

class UserSchema(pyBaseModel):
    name: str = ""
    email: str = ""
    password: str = ""
    phone: str = ""
