from pydantic import BaseModel, field_validator, EmailStr
from typing import Optional
from enum import Enum
from datetime import datetime
from core import exceptions


class SignupUser(BaseModel):
    username: str
    email: EmailStr
    password: str


    @field_validator("username")
    @classmethod
    def username_field(cls, v: str):
        if len(v) < 5:
            raise exceptions.ShortUsername
        
        elif len(v) > 55:
            raise exceptions.LongUsername
        
        return v

    @field_validator("password")
    @classmethod
    def password_field(cls, v: str):
        if len(v) < 8:
            raise exceptions.ShortPassword
        
        elif len(v) > 55:
            raise exceptions.LongPassord
        
        return v
