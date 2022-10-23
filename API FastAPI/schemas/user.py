from socket import AI_NUMERICHOST
<<<<<<< HEAD
from typing import Any, Optional, Union, Optional
from datetime import datetime
from pydantic import BaseModel as pyBaseModel

class Token(pyBaseModel):
    access_token: str
    token_type: str


class TokenData(pyBaseModel):
    email: Union[str, None] = None
=======
from typing import Any, Union
from datetime import datetime
from pydantic import BaseModel as pyBaseModel

class UserSchemaCreation(pyBaseModel):
    id: int
    name: str = ""
    email: str = ""
    password: str = ""
    phone: str = ""
    created_at: Any
    updated_at: Any
>>>>>>> origin/floapp

class UserSchema(pyBaseModel):
    id: int
    name: str = ""
    email: str = ""
    password: str = ""
    phone: str = ""
    created_at: Any
    updated_at: Any
    status: Optional[bool] = None

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


<<<<<<< HEAD
class UserInDB(UserSchema):
    hashed_password: str

class UserSchemaAuth(pyBaseModel):
    email: str
    password: str
=======
>>>>>>> origin/floapp
