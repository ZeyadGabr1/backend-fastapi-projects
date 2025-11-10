from passlib.context import CryptContext


class Hash:

    pwd = CryptContext(schemes=['bcrypt'])

    @classmethod
    def encrypt(cls, password: str):
        return cls.pwd.hash(password)
    
