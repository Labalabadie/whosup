from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean, JSON
from config.db import meta, engine
from datetime import datetime

event = Table("event", meta, 
    Column("id", Integer, primary_key=True), ## unica
    Column("name", String(255)),

    Column("event_host", String(255)),
    Column("event_datetime", DateTime),
    Column("location", String(255)),
    Column("description", String(255)),
    Column("icon", String(15)),
    Column("max_people", Integer),
    Column("participants", String(255)), ## related con user.id

    Column("config", JSON),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow),
    Column("status", Boolean, default=True))

meta.create_all(engine)