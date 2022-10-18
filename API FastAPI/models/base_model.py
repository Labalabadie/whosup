from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, DateTime
from config.db import meta, conn

Base = declarative_base(metadata=meta)

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    
    @classmethod
    def to_dict(cls): 
        return {c.name: getattr(cls, c.name) for c in cls.__table__.columns} 
    ##

    @classmethod
    def _get(cls, id=None):
        if id is not None:
            conn.execute(select(cls.__class__).where(cls.__class__.id == id))
        else:
            conn.execute(select(cls.__class__))