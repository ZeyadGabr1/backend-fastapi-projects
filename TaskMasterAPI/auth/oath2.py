from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime
from jose import jwt, JWTError
from fastapi import Depends
from fastapi import HTTPException, status
from db.db_user import UserFunc
from db.connection import get_db
from sqlalchemy.orm import Session

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')
SECRET_KEY = '3d5766105e02fc7f65d13b461775bd8e46f28eae2e13acce58219651c7ae0767'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE = 30

manage = UserFunc()

def create_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=15) # !!

    to_encode.update({
        'exp': expire
    })

    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return access_token


def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):

    validtion_error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                    detail='Data Validtion Error')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id : int = payload.get('user_id')
        if user_id is None:
            raise validtion_error
        
    except JWTError:
        raise validtion_error
    
    user = manage.get_user_by_id(user_id, db)

    if user is None:
        raise validtion_error
    
    return user





    

