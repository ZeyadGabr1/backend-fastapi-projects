from fastapi import APIRouter, Depends
from routes.schemas import  ProductBase, ProductDisplay
from sqlalchemy.orm import Session
from db.connection.connection import get_db
from db.db_oprations.db_products import ProductManage
from auth.oath2 import get_current_user
from db.models import DbUser
from typing import List


router = APIRouter(
    prefix='/product',
    tags=['products']
)

product_manage = ProductManage()


@router.get('/all')
def get_all_products(db: Session = Depends(get_db), user: DbUser = Depends(get_current_user)):
    return product_manage.show_all_products(user, db)

@router.post('/add', response_model=ProductBase)
def add_new_product(request: ProductBase, user: DbUser = Depends(get_current_user), db: Session = Depends(get_db)):
    return product_manage.add_product(user, request, db)

@router.delete('/delete/{id}')
def delete_product(id: int, user: DbUser = Depends(get_current_user), db: Session = Depends(get_db)):
    return product_manage.delete_product(user, id, db)

@router.put('/edit/{id}')
def edit_product(id: int, request: ProductBase, user: DbUser = Depends(get_current_user), db: Session = Depends(get_db)):
    return product_manage.edit_product(user, id, request, db)


@router.get('/search', response_model=List[ProductDisplay])
def filter_search(user: DbUser = Depends(get_current_user),
                   price: int = 50, 
                   stock: int = 1,
                   db: Session = Depends(get_db)):
    
    return product_manage.search(user, price, stock, db)