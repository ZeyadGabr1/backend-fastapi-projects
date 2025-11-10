from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Database  Url Localy
DATABASE_URL = 'sqlite:///./data'

# Engine ---> Responsbile For All Oprations In Database
engine = create_engine(DATABASE_URL)

# Responsbile For Making Session With Database Using Engine
Session_local = sessionmaker(bind=engine)

# For Define All Tables In Database
Base = declarative_base()


def get_db():
    """Making Session With db And return it and after opration close db"""

    db = Session_local()

    try:
        yield db

    finally:
        db.close()