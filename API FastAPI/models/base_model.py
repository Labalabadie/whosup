from datetime import datetime
from sqlalchemy import Integer, Column, String, DateTime
from config.db import meta, conn, Base
from sqlalchemy import insert, select, update, delete, join



class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    @staticmethod
    def to_dict(cls): 
        return {c.name: getattr(cls, c.name) for c in cls.__table__.columns} 
    ##

    @staticmethod
    def _get(cls, id=None):
        if id is not None:
            conn.execute(select(cls).where(cls.id == id))
        else:
            conn.execute(select(cls))