from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, Integer,  String, DateTime, JSON
from datetime import datetime
from models.base_model import BaseModel, Base
from config.db import engine, meta


class Notification(BaseModel): 
    __tablename__ = "notification" 
    text = Column(String(255))

    
    @classmethod
    def attrs(cls, str=None):
        """ Returns a list of or attributes for the given class """
        base_attrs = BaseModel.attrs()

        public_attrs = [
                "text"]

        return base_attrs + public_attrs
