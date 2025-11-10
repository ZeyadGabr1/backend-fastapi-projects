from sqlalchemy.orm import Session
from routes.schemas import UserBase, ChangePassword
from db.models import DbUser
from auth.hashing import Hash
from db.db_oprations.exptions import Exptions


exption = Exptions()


class UserManage:

    def get_user_by_id(self, user_id: int, db: Session):
        return db.query(DbUser).filter(DbUser.id == user_id).one_or_none()


    def get_my_profile(self, user: DbUser):
        
        if not user:
            raise exption.login_required()
        
        return user
    
    def register(self, request: UserBase, db: Session):

        email = db.query(DbUser).filter(DbUser.email == request.email).one_or_none()

        if email:
            raise exption.email_exists()

        hashed_password = Hash.hash_password(request.password)

        user = DbUser(
            username=request.username,
            email=request.email,
            hashed_password=hashed_password
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return  user


    def get_orders(self, user: DbUser):
        return user.orders
    

    def change_username(self, user: DbUser, new_username: str, db: Session):

        if not user:
            raise exption.login_required()
        
        user.username = new_username
        db.commit()
        return {
            "status": "Successful",
            "msg": "Username Updated Successfuly"
        }
    
    def change_email(self, user: DbUser, new_email: str, db: Session):

        if not user:
            raise exption.login_required()
        
        email = db.query(DbUser).filter(DbUser.email == new_email).one_or_none()

        if email:
            raise exption.email_exists()
        
        else: 
            user.email = new_email
            db.commit()
            return {
                "status": "Successful",
                "msg": "Email Updated Successfuly"
            }
        
    def change_password(self, user: DbUser, request: ChangePassword, db: Session):

        if not user:
            raise exption.login_required()
        
        elif not Hash.verify_password(request.current_password, user.hashed_password):
            raise exption.wrong_password()
        
        else:
            user.hashed_password = Hash.hash_password(request.new_password)
            db.commit()
            return {
                "status": "Successful",
                "msg": "Password Updated Successfuly"
            }
        
    def delete_user(self, user: DbUser, db: Session):

        if not user:
            raise exption.login_required()
        
        else:
            db.delete(user)
            db.commit()
            return {
                "msg": "Removed Done"
            }
