from email.policy import default
from sqlalchemy import Column, ForeignKey
from models.user_rel import joined_groups_rel
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from datetime import datetime
from models.base_model import BaseModel
from config.db import engine, meta

class Group(BaseModel):
    __tablename__ = "group"
    name = Column(String(255))
    description = Column(String(255))
    
    group_id = Column(Integer)
    group_admin_id = Column(Integer, ForeignKey('user_data.id'), nullable=False)
    group_admin = relationship('User', back_populates='admin_groups')
    
    #group_members = relationship('User', secondary=joined_groups_rel, back_populates='joined_groups')
    #members_id = Column(Integer, ForeignKey('user_data.id'))
    #members = Column(Integer, )
    
    status = Column(Boolean, default=True)

    @classmethod
    def attrs(cls, str=None):
        """ Returns a list of or attributes for the given class """
        base_attrs = BaseModel.attrs()

        public_attrs = [
                "name",
                "status"]
        