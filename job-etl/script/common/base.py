from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
)
session = Session(engine)
Base = declarative_base()