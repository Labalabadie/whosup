from email.policy import default
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from datetime import datetime
from models.base_model import BaseModel

class User(BaseModel):
    __tablename__ = "user_data"
    name = Column(String(255))

    email = Column(String(255))
    password = Column(String(255))
    phone = Column(String(255))

    #Column("login_token", String(255)),
    status = Column(Boolean, default=True)

    # Relations --