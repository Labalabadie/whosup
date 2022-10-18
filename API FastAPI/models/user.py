from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from models.base_model import BaseModel, Base

attending_event_rel = Table(
    "attending_event_rel",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user_data.id"), primary_key=True),
    Column("event_id", Integer, ForeignKey("event.id"), primary_key=True),
    extend_existing=True
)

class User(BaseModel):
    __tablename__ = "user_data"
    name = Column(String(255))

    email = Column(String(255))
    password = Column(String(255))
    phone = Column(String(255))

    #Column("login_token", String(255)),
    status = Column(Boolean, default=True)

    # Relationships --
    hosted_events = relationship('Event', back_populates='event_host')
    attending_events = relationship("Event", secondary=attending_event_rel, back_populates='participants')
    admin_groups = relationship('Group', back_populates='group_admin')
    admin_channels = relationship('Channel', back_populates='channel_admin')

    @classmethod
    def attrs(cls, str=None):
        """ Returns a list of or attributes for the given class """
        base_attrs = cls.super().attrs()

        public_attrs = [
                "name",
                "email",
                "phone",
                "status"]

        priv_attrs = [
                "hosted_events",
                "attending_events",
                "admin_groups",
                "admin_channels"]
        
        sys_excl = ["password"]

        if str == None:
            return base_attrs + public_attrs
        elif str == "priv":
            return base_attrs + public_attrs + priv_attrs