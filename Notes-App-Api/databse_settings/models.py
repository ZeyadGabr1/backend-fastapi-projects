from .settings import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class DbUsers(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())   

    notes = relationship("Notes", back_populates="user", cascade="all, delete-orphan")


class Notes(Base):

    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    content = Column(String(255), nullable=False)
    added_at = Column(DateTime, default=datetime.now())


    user = relationship("DbUsers", back_populates="notes")


