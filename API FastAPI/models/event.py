from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean, JSON
from datetime import datetime
from models.base_model import Base

class Event(Base): 
    __tablename__ = "event" 
    id = Column(Integer, primary_key=True) ## unica
    name = Column(String(255))

    event_host = Column(Integer, nullable=False)
    event_datetime = Column(DateTime)
    location = Column(String(255))
    description = Column(String(255))
    icon = Column(String(2))
    max_people = Column(Integer, default=1)
    participants = Column(String(255)) ## related con user.id

    config = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    status = Column(Boolean, default=True)