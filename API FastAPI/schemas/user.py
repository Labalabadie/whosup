<<<<<<< HEAD
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str
    phone: str

=======
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str
    phone: str

>>>>>>> 2f9ef4324d3b07ca3809107279c7e760baae2a72
    