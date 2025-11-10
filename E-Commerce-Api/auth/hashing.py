from passlib.context import CryptContext




class Hash:

    pwd = CryptContext(schemes=['bcrypt'])

    @classmethod
    def hash_password(cls, password: str):
        return cls.pwd.hash(password)
    
    @classmethod
    def verify_password(cls, input_password, stored_password):
        return cls.pwd.verify(input_password, stored_password)
    
    