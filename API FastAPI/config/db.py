<<<<<<< HEAD
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost:3306/storedb")

meta = MetaData()

conn = engine.connect()
=======
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://dev:password@localhost:3306/storedb")

meta = MetaData()

conn = engine.connect()
>>>>>>> 2f9ef4324d3b07ca3809107279c7e760baae2a72
