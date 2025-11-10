from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from db.connection.confige import DB_URL


DATABASE_URL = DB_URL

if DATABASE_URL is None:

    DATABASE_URL = "sqlite:///data.db"


engine = create_engine(DATABASE_URL)

Session_local = sessionmaker(bind=engine)

Base = declarative_base()

if "sqlite" in DATABASE_URL:
    Base.metadata.create_all(engine)

def get_db():

    db = Session_local()

    try:
        yield db

    finally:
        db.close()