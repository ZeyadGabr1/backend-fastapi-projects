from fastapi import APIRouter, Depends
from routes.schemas import OrderBase, OrderDisplay, OrderStatus
from sqlalchemy.orm import Session
from db.connection.connection import get_db
from db.db_oprations.db_orders import OrderManager
from auth.oath2 import get_current_user
from db.models import DbUser
from typing import List


router = APIRouter(
    prefix='/order',
    tags=['orders']
)

order_manage = OrderManager()

@router.get('/my', response_model=List[OrderDisplay])
def get_my_orders(user: DbUser = Depends(get_current_user), db: Session = Depends(get_db)):
    return order_manage.get_my_orders(user, db)


@router.post('/create')
def create_order(request: OrderBase, user: DbUser = Depends(get_current_user), db: Session = Depends(get_db)):
    return order_manage.place_order(user, request, db)


@router.put('/update/status/{id}')
def update_status(id: int, request: OrderStatus, 
                  user: DbUser = Depends(get_current_user),
                   db: Session = Depends(get_db)):
    
    return order_manage.update_order_status(id, user, request, db)


@router.get('/all')
def get_all_orders(user: DbUser = Depends(get_current_user)
                   , db: Session = Depends(get_db)):
    
    return order_manage.show_all_orders(user, db)

@router.get('/search', response_model=List[OrderDisplay])
def filter_search(user: DbUser = Depends(get_current_user),
                  status: OrderStatus = OrderStatus.under_review,
                   db: Session = Depends(get_db)):
    
    return order_manage.search(user, status, db)