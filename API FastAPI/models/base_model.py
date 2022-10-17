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

    def to_dict(self): 
        return {c.name: getattr(self, c.name) for c in self.__table__.columns} 

    def _get(self, id=NULL):
        if id is not NULL:
            conn.execute(select(self.__class__).where(self.__class__.id == id))
        else:
            conn.execute(select(self.__class__))