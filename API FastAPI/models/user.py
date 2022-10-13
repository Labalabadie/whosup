from email.policy import default
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from datetime import datetime
from models.base_model import BaseModel
from config.db import engine, meta
class User(BaseModel):
    __tablename__ = "user_data"
    name = Column(String(255))

    email = Column(String(255))
    password = Column(String(255))
    phone = Column(String(255))

    #Column("login_token", String(255)),
    status = Column(Boolean, default=True)

    # Relations --
    hosted_events = relationship('Event', back_populates='event_host')
    admin_groups = relationship('Group', back_populates='group_admin')
    admin_channels = relationship('Channel', back_populates='channel_admin')
