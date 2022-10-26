from sqlalchemy import Table, Column, ForeignKey
from .user_rel import attending_event_rel#, contact_rel
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from models.base_model import BaseModel, Base

class User(BaseModel):
    __tablename__ = "user_data"
    name = Column(String(255))

    email = Column(String(255), unique=True)
    password = Column(String(255))
    phone = Column(String(255))

    #Column("login_token", String(255)),
    status = Column(Boolean, default=True)

    # Relationships --
    hosted_events = relationship('Event', back_populates='event_host')
    attending_events = relationship("Event", secondary=attending_event_rel, back_populates='participants')
    #contacts = relationship("User", secondary=contact_rel, primarjoin=User.id==contact_rel.c.user_id)
    #in_contacts_of = relationship("User", secondary=contact_rel, back_populates='contacts')
    admin_groups = relationship('Group', back_populates='group_admin')
    admin_channels = relationship('Channel', back_populates='channel_admin')

    @classmethod
    def attrs(cls, str=None):
        """ Returns a list of or attributes for the given class """
        base_attrs = BaseModel.attrs()

        public_attrs = [
                "name",
                "email",
                "phone",
                "status"]

        priv_attrs = [
                "hosted_events",
                "attending_events",
                "admin_groups",
                "admin_channels"
                #"contacts",
                #"in_contacts_of"
                ]
        
        sys_excl = ["password"]

        if str == None:
            return base_attrs + public_attrs
        elif str == "all":
            return base_attrs + public_attrs + priv_attrs
        elif str == "rel":
            return priv_attrs
