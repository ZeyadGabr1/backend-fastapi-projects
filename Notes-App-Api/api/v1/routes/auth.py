from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from databse_settings.settings import get_db
from services.auth_service import AuthService
from schemas.users import SignupUser

from core.decorators import logging_decorator



router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)

auth_service = AuthService()


@router.post("/login")
def user_login(response: Response, request: OAuth2PasswordRequestForm = Depends(),  db: Session = Depends(get_db)):
    return auth_service.login(request, response, db)

@router.post('/signup')
def user_signup(data: SignupUser, db: Session = Depends(get_db)):
    return auth_service.signup(data, db)

