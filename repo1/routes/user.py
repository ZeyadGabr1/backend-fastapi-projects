from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
import modelus
from hashing import Hash
from schemas import *
from typing import List

router = APIRouter(
    prefix='/user',
    tags=['users']
)

@router.get('/show_users', response_model=List[ShowUser])
def show_users(db: Session = Depends(get_db)):
    return db.query(modelus.Users).all()


@router.post('/new_user')
def add_user(request:User, db: Session = Depends(get_db)):

    hashed_password = Hash.encrypt(request.password)
    new_user = modelus.Users(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.delete('/del_user/{id}', status_code=status.HTTP_200_OK)
def delete_user(id, db: Session = Depends(get_db)):

    user = db.query(modelus.Users).filter(modelus.Users.id == id)

    if user.first():
        user.delete()
        db.commit()
        return {'detail': 'Removed Done'}
    
    return {'detail': 'User Not Found'}

