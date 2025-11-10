from database import Base
from sqlalchemy import Column, String, INTEGER

class Users(Base):

    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    