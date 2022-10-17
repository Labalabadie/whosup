from email.policy import default
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from datetime import datetime
from models.base_model import BaseModel, Base

attending_event_rel = Table(
    "attending_event_rel",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user_data.id"), primary_key=True),
    Column("event_id", Integer, ForeignKey("event.id"), primary_key=True)
)

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
    attending_events = relationship("Event", secondary=attending_event_rel, back_populates='participants')
    admin_groups = relationship('Group', back_populates='group_admin')
    admin_channels = relationship('Channel', back_populates='channel_admin')

