# Sqlalchemy
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, Date

# App
from config.db import meta, engine

users = Table("users", meta, 
    Column("user_id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("Email", String(255)),
    Column("password", String(255)),
    Column("streamer", Boolean(False)),
    Column("birth_date", Date),
    Column("videos", Boolean(False))
    )

meta.create_all(engine)