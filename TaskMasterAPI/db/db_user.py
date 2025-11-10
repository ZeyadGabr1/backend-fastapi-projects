from routes.schemas import UserBase, EditUser
from sqlalchemy.orm import Session
from db.models import DbUser
from auth.hashing import Hash
from fastapi import HTTPException, status


class UserFunc:

    
    def add_user(self, request: UserBase, db: Session):

        hashed_password = Hash.hashing(request.password)
        new_user = DbUser(
        username=request.username,
        email=request.email,
        hashed_password=hashed_password
    )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    def get_user(self, id: int, db: Session):

        user = db.query(DbUser).filter(DbUser.id == id).one_or_none()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'User With Id : {id} Not Found'
        )
    
        return user
    

    def delete_user(self, id: int, db: Session):

        user = db.query(DbUser).filter(DbUser.id == id).one_or_none()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'User With Id : {id} Not Found'
        )
    
        db.delete(user)
        db.commit()

        return {
            "msg": "User Removed Done"
        }
    

    def update_user(self, user: DbUser, request: EditUser, db: Session):

        

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'User With Id : {user.id} Not Found'
            )
        
        user.username = request.username
        user.email = request.email

        db.commit()
        return {
            'msg': 'User Updated Done'
        }
    

    def get_user_by_id(self, id: int, db: Session):

        user = db.query(DbUser).filter(DbUser.id == id).one_or_none()

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='User Not Found')
        
        return user