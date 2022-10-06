<<<<<<< HEAD
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

users = Table("users", meta, Column(
    "id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
    Column("phone", String(255)))

meta.create_all(engine)
=======
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

users = Table("users", meta, Column(
    "id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
    Column("phone", String(255)))

meta.create_all(engine)
>>>>>>> 2f9ef4324d3b07ca3809107279c7e760baae2a72
