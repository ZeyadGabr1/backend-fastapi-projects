from pydantic import BaseModel, field_validator
from typing import  Optional
from enum import Enum
from datetime import datetime
from core import exceptions




class NotesCategories(str, Enum):
    work = "work"
    study = "study"
    personal = "personal"



class AddNote(BaseModel):
    title: str
    content: str

    @field_validator("title")
    @classmethod
    def title_field(cls, v: str):
        if len(v) < 5:
            raise exceptions.ShortTitle
        
        elif len(v) > 55:
            raise exceptions.LongTitle
        
        return v
    
    @field_validator("content")
    @classmethod
    def content_field(cls, v: str):
        if len(v) < 15:
            raise exceptions.ShortContent
        
        elif len(v) > 255:
            raise exceptions.LongContent
    
        return v


class UpdateNote(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

    @field_validator("title")
    @classmethod
    def title_field(cls, v: str):
        if len(v) < 5:
            raise exceptions.ShortTitle
        
        elif len(v) > 55:
            raise exceptions.LongTitle
        
        return v
    
    @field_validator("content")
    @classmethod
    def content_field(cls, v: str):
        if len(v) < 15:
            raise exceptions.ShortContent
        
        elif len(v) > 255:
            raise exceptions.LongContent
    
        return v


class DisplayNotes(BaseModel):
    id: int
    title: str
    content: str
    category: str
    added_at: datetime


