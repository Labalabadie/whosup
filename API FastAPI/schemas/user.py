from typing import Optional
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    password: str
    phone: str

    
