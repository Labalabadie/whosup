from typing import Optional
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str
    phone: str

    
