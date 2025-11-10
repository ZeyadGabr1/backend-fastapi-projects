from db.connection.connection import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from routes.schemas import  OrderStatus


class DbUser(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

    orders = relationship('DbOrders', back_populates='user')
    products = relationship('DbProducts', back_populates='user')


class DbProducts(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('DbUser', back_populates='products')
    order = relationship('DbOrders', back_populates='product')


class DbOrders(Base):

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    price = Column(Integer, nullable=False)
    status = Column(String(30), default=OrderStatus.under_review)
    capcity = Column(Integer)

    user = relationship('DbUser', back_populates='orders')
    product = relationship('DbProducts', back_populates='order')
