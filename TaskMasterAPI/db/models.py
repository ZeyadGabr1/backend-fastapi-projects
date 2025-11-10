from db.connection import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class DbUser(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)

    tasks = relationship('DbTask', back_populates='user')

class DbTask(Base):

    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('DbUser', back_populates='tasks')