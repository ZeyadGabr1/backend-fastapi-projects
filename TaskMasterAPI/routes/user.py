from fastapi import APIRouter, Depends, HTTPException, status
from routes.schemas import UserBase, UserDisplay, EditUser
from sqlalchemy.orm import Session
from db.connection import get_db
from db.db_user import UserFunc
from auth.oath2 import oauth2_schema, get_current_user
from db.models import DbUser

router = APIRouter(
    prefix='/user',
    tags=['user']
)

user_manage = UserFunc()

@router.post('/create', response_model=UserDisplay)
def add_user(request: UserBase, db: Session = Depends(get_db)):
    return user_manage.add_user(request, db)



@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
    return user_manage.get_user(id, db)


@router.delete('/delete/{id}')
def delete_user(id: int, db: Session = Depends(get_db), user: DbUser = Depends(get_current_user)):
    
    if user.id != id:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail='You Are Not The Creator')
    
    return user_manage.delete_user(id, db)



@router.put('/update/{id}')
def update_user(request: EditUser, user: DbUser = Depends(get_current_user), db: Session = Depends(get_db)):
    return user_manage.update_user(user, request, db)



