from datetime import datetime
from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy.sql.sqltypes import Boolean, Integer,  String, DateTime, JSON
from config.db import meta, conn, Base
from sqlalchemy import insert, select, update, delete, join



class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    status = Column(Boolean, default=True)

    def to_dict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

    @classmethod
    def attrs(cls, str=None):
        attrs = ["id", "created_at", "updated_at"]
        return attrs

    """ def to_dict(self): 
        return {c.name: getattr(self, c.name) for c in self.__table__.columns} 
    ##

    
    def _get(self, id=None):
        if id is not None:
            conn.execute(select(self.__class__).where(self.__class__.id == id))
        else:
            conn.execute(select(self.__class__))"""