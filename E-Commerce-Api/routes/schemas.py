from pydantic import BaseModel, Field
from enum import Enum
from typing import List

# ------------------------------------------------------------------------------
# inputs: 


class UserBase(BaseModel):

    username: str = Field(min_length=8, max_length=30)
    email: str = Field(min_length=8, max_length=50)
    password: str = Field(min_length=8)

    class Username(BaseModel):
        username: str = Field(min_length=8, max_length=30)

    class Email(BaseModel):
        email: str = Field(min_length=8, max_length=50)


class ChangePassword(BaseModel):
    current_password: str = Field(min_length=8)
    new_password: str = Field(min_length=8)

    

class ProductBase(BaseModel):

    name: str = Field(min_length=4, max_length=30)
    description: str = Field(min_length=30, max_length=255)
    price: int
    stock: int


class OrderBase(BaseModel):

    product_id: int
    capcity: int


class OrderStatus(Enum):
    
    canceled = 'Canceled'
    under_review = 'Under review'
    shipped = 'Shipped'




# ------------------------------------------------------------------------------
# Responses: 

class ProductDisplay(BaseModel):

    id: int
    name: str
    description: str
    price: int
    stock: int

class OrderDisplay(BaseModel):

    id: int
    user_id: int
    product_id: int
    price: int
    status: str
    capcity: int

class UserDisplay(BaseModel):
    
    id: int
    username: str
    email: str
    products: List[ProductDisplay] = []
    orders: List[OrderDisplay] = []


