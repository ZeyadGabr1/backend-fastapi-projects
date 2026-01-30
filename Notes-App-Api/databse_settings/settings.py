from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
Base = declarative_base()



def get_db():
    try:
        db = Session()
        yield db

    finally:
        db.close()
