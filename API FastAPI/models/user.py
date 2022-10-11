from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

user_data = Table("user_data", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("created_at", String(255)),
    Column("updated_at", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
    Column("phone", String(255)),
    #Column("login_token", String(255)),
    Column("status", Boolean))
 
meta.create_all(engine)
