from email.policy import default
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from datetime import datetime
from models.base_model import BaseModel
from config.db import engine, meta
class Channel(BaseModel):
    __tablename__ = "channel"
    name = Column(String(255))

    description = Column(String(255))
    admin = Column(Integer, ForeignKey('user_data.id'))
    
    #Column("login_token", String(255)),
    #status = Column(Boolean, default=True)

    # Relations --
    channel_admin = relationship('User', back_populates='admin_channels')
    channel_admin_id = Column(Integer, ForeignKey('user_data.id'), nullable=False) # user.id == User.id (class)
