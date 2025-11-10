from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth.oath2 import create_token
from db.models import DbUser
from db.connection import get_db
from sqlalchemy.orm import Session
from auth.hashing import Hash

router = APIRouter(
    tags=['authentication']
)


@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    data_exption = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Data Is Incorrect! Please Try Again'
    )
    
    user = db.query(DbUser).filter(DbUser.email == request.username).one_or_none()

    if not user:
        raise data_exption
    
    elif not Hash.verify(request.password, user.hashed_password):
        raise data_exption
    
    access_token = create_token({'user_id': user.id})
    
    return {
        'access_token': access_token,
        'user_id': user.id}

