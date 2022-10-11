from email.policy import default
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from config.db import meta, engine
from datetime import datetime

user_data = Table("user_data", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),

    Column("email", String(255)),
    Column("password", String(255)),
    Column("phone", String(255)),

    #Column("login_token", String(255)),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow),
    Column("status", Boolean, default=True))
 
meta.create_all(engine)
