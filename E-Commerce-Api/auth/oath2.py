from fastapi.security import OAuth2PasswordBearer
from db.connection.confige import JWT_SECRET, JWT_ALGORITHM
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status, Cookie
from sqlalchemy.orm import Session
from db.connection.connection import get_db
from db.db_oprations.db_user import UserManage


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

user_manage = UserManage()

def create_access_token(data: dict):

    to_encode = data.copy()


    expire = datetime.utcnow() +  timedelta(minutes=15)

    to_encode.update({
        'exp': expire
    })

    access_token = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return access_token


def get_current_user(token: str =  Depends(oauth2_scheme), db: Session = Depends(get_db)):

    data_exption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                 detail='invalid Token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='UnAuthorized')
    
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = payload.get('user_id')

        if user_id is None:
            raise data_exption
        
    except JWTError:
        raise data_exption
    
    user = user_manage.get_user_by_id(user_id, db)

    if user is None:
        raise data_exption
    
    return user
        




