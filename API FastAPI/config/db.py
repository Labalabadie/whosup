from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://dev:password@localhost:3306/storedb")

meta = MetaData()

conn = engine.connect()

Base = declarative_base(metadata=meta)

Session = sessionmaker(bind=engine, autoflush=True, transactional=True)
sess = Session()