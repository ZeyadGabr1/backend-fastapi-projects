from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.connection.connection import get_db
from db.models import DbUser
from auth.hashing import Hash
from auth.oath2 import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['authentecator']
)


@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(DbUser).filter(DbUser.email == request.username).one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User Not Found! Please Sign Up')
    
    elif not Hash.verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Password Was Incorrect!')
    
    
    access_token = create_access_token({'user_id': user.id})


    return {
        'msg': 'Loging Succsefuly',
        'access_token': access_token,
        'is_admin': user.is_admin
        }


