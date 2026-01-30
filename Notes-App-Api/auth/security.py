from passlib.context import CryptContext
from core.decorators import logging_decorator


pwd_context = CryptContext(schemes=["bcrypt"])


class Security:
    
    @logging_decorator
    def hash_password(self, password: str) -> str:
        try:
            return pwd_context.hash(password)

        except Exception as e:
            print(password)
            raise e

    
    @logging_decorator
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
