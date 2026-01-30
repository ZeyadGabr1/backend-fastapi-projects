from sqlalchemy.orm import Session
from schemas.notes import AddNote, NotesCategories, UpdateNote
from databse_settings.models import DbUsers
from core import exceptions
from typing import Optional
from auth.security import Security
from auth.config import create_access_token, create_refresh_token

from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import Response

from schemas.users import SignupUser



security = Security()


class AuthService:

    def login(self, request: OAuth2PasswordRequestForm, response: Response, db: Session):
        user = db.query(DbUsers).filter(DbUsers.email == request.username).one_or_none()

        if not user:
            raise exceptions.UserNotFound
        
        elif not security.verify_password(request.password, user.hashed_password):
            raise exceptions.IncorrectPassword
        

        data = {
            "user_id": user.id
        }
        access_token = create_access_token(data)
        refresh_token = create_refresh_token(data)
        
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=False,
            samesite="lax",
            max_age=60 * 15
        )

        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=False,
            samesite="lax",
            max_age=60 * 60 * 24 * 7
        )

        return user


    def signup(self, data: SignupUser, db: Session):
        user = db.query(DbUsers).filter(DbUsers.email == data.email).one_or_none()

        if user:
            raise exceptions.UserRegistered
        
        #print(data.password)
        
        hashed_password = security.hash_password(data.password)
        
        new_user = DbUsers(username=data.username,
                           email=data.email,
                           hashed_password=hashed_password)
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return user
        


