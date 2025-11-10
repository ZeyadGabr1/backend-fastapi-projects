from fastapi import APIRouter, Depends
from routes.schemas import UserBase, UserDisplay, ChangePassword
from sqlalchemy.orm import Session
from db.connection.connection import get_db
from db.db_oprations.db_user import UserManage
from auth.oath2 import get_current_user
from db.models import DbUser


router = APIRouter(
    prefix='/user',
    tags=['user']
)


user_manage = UserManage()

@router.get('/me', response_model=UserDisplay)
def get_my_profile(user: DbUser = Depends(get_current_user)):
    return user_manage.get_my_profile(user)


@router.post('/reigster', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return user_manage.register(request, db)


@router.get('/orders')
def get_my_orders(user: DbUser = Depends(get_current_user)):
    return user_manage.get_orders(user)


@router.put('/update/username')
def update_username(request: UserBase.Username,
                     user: DbUser = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    
    return user_manage.change_username(user, request.username, db)

@router.put('/update/email')
def update_email(request: UserBase.Email,
                     user: DbUser = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    
    return user_manage.change_email(user, request.email, db)

@router.put('/update/password')
def update_email(request: ChangePassword,
                     user: DbUser = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    
    return user_manage.change_password(user, request, db)


@router.delete('/delete')
def delete_user(user: DbUser = Depends(get_current_user),
                db: Session = Depends(get_db)):
    
    return user_manage.delete_user(user, db)