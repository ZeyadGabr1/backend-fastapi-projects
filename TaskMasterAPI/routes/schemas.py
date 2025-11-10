from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from fastapi import Body

class TaskBase(BaseModel):

    """ When User Add Task"""

    title: str 
    description: str
    deadline: datetime
    

class UpdateTask(BaseModel):

    title: str 
    description: str
    deadline: datetime
    
    
class UserBase(BaseModel):
    """ When User reigster """

    username: str
    email: str 
    password: str 
    


class UserDisplay(BaseModel):
    
    username: str
    tasks: List[TaskBase] = []


class EditUser(BaseModel):

    username: str
    email: str
    

