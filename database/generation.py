from sqlalchemy import text
from .model import Base
from .connection import engine


def ensure_schema(schema: str):
    with engine.begin() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))


def ensure_table():
    Base.metadata.create_all(engine)


def ensure_db_ready(schema: str = "iot"):
    ensure_schema(schema=schema)
    ensure_table()
