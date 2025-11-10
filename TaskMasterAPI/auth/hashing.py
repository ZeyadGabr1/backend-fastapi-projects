from passlib.context import CryptContext


class Hash:

    pwd = CryptContext(schemes=['bcrypt'])

    @classmethod
    def hashing(cls, password: str):
        return cls.pwd.hash(password)
    
    @classmethod
    def verify(cls, input_password: str, stored_password: str):
        return cls.pwd.verify(input_password, stored_password)
    
        