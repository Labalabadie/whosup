from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, DateTime
from config.db import meta

Base = declarative_base(metadata=meta)

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
