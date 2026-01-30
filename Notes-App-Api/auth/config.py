from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt, JWTError
from dotenv import load_dotenv
from fastapi import Request, Response, Depends
from databse_settings.settings import get_db
from sqlalchemy.orm import Session
from databse_settings.models import DbUsers
import os


load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
ACCESS_TOKEN_SECRET_KEY = os.getenv("ACCESS_TOKEN_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

REFRESH_TOKEN_EXPIRE_DAYS = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")
REFRESH_TOKEN_SECRET_KEY = os.getenv("REFRESH_TOKEN_SECRET_KEY")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    )

    to_encode.update({
        "exp": expire,
        "type": "access"
    })

    encoded_jwt = jwt.encode(to_encode, ACCESS_TOKEN_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



def create_refresh_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(days=int(REFRESH_TOKEN_EXPIRE_DAYS))

    to_encode.update({
        "exp": expire,
        "type": "refresh"
    })

    encoded_jwt = jwt.encode(to_encode, REFRESH_TOKEN_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str, secret: str):
    try:
        return jwt.decode(token, secret, algorithms=[ALGORITHM])
    except JWTError:
        return None



def get_remaining_seconds(payload: dict) -> int:
    exp = payload.get("exp")
    if not exp:
        return 0
    now = datetime.now(tz=timezone.utc).timestamp()
    return int(exp - now)


async def get_current_user(
    request: Request,
    response: Response,
    db: Session = Depends(get_db)
):
    access_token = request.cookies.get("access_token")
    refresh_token = request.cookies.get("refresh_token")

    if access_token:
        payload = decode_token(access_token, ACCESS_TOKEN_SECRET_KEY)

        if payload:
            remaining = get_remaining_seconds(payload)

            if remaining > 120:
                user_id = payload.get("user_id")
                return get_user_by_id(db, user_id)

    if refresh_token:
        refresh_payload = decode_token(
            refresh_token,
            REFRESH_TOKEN_SECRET_KEY
        )

        if refresh_payload:
            user_id = refresh_payload.get("user_id")

            user = get_user_by_id(db, user_id)
            if not user:
                return None

            # توليد access جديد
            new_access_token = create_access_token(
                data={"user_id": user.id}
            )

            response.set_cookie(
                key="access_token",
                value=new_access_token,
                httponly=True,
                secure=False,   
                samesite="lax",
                max_age=60 * 15
            )

            return user

    return None


def get_user_by_id(db: Session, id: int):
    return db.query(DbUsers).filter(DbUsers.id == id).one_or_none()