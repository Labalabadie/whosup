from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

event = Table("event", meta, Column(
    "id", Integer, primary_key=True), ## unica
    Column("event_name", String(255)),
    Column("event_datetime", String(255)),
    Column("location", String(255)),
    Column("description", String(255)),
    Column("participants", String(255)), ## related con user.id
    Column("event_status", String(255)),
    Column("nonolist", String(255)))

meta.create_all(engine)