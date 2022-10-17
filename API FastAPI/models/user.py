from email.policy import default
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from datetime import datetime
from models.base_model import BaseModel
from models.event import AttendingEventRel

class User(BaseModel):
    __tablename__ = "user_data"
    name = Column(String(255))

    email = Column(String(255))
    password = Column(String(255))
    phone = Column(String(255))

    #Column("login_token", String(255)),
    status = Column(Boolean, default=True)

    # Relationships --
    hosted_events = relationship('Event', back_populates='event_host')
    attending_events = relationship("Event", secondary=AttendingEventRel, back_populates='participants')
    admin_groups = relationship('Group', back_populates='group_admin')
    admin_channels = relationship('Channel', back_populates='channel_admin')

