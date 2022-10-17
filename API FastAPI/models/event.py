from email.policy import default
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean, JSON
from datetime import datetime
from models.base_model import BaseModel, Base
from config.db import engine, meta


class AttendingEventRel(Base):
    __tablename___ = 'attending_event_rel'
    user_id = Column("user_id", Integer, ForeignKey("user_data.id"))
    event_id = Column("event_id", Integer, ForeignKey("event.id"))


class Event(BaseModel): 
    __tablename__ = "event" 
    name = Column(String(255))

    event_host_id = Column(Integer, ForeignKey('user_data.id'), nullable=False) # user.id == User.id (class)
    event_host = relationship("User", back_populates="hosted_events")

    event_datetime = Column(DateTime)
    location = Column(String(255))
    description = Column(String(255))
    icon = Column(String(2))
    max_people = Column(Integer, default=1)
    participants = relationship("User", secondary=attending_event_rel, back_populates='attending_events') ## related con user.id

    group_id = Column(Integer, ForeignKey('group.id'), default=None)
    channel_id = Column(Integer, ForeignKey('channel.id'), default=None)

    config = Column(JSON)
    status = Column(Boolean, default=True)
