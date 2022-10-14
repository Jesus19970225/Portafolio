from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:1997jesus122333@localhost:3306/dbfastapi")

meta = MetaData()

conn = engine.connect()