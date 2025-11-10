import os
from dotenv import load_dotenv


# ----------------------------------------------------

# load all Variables
load_dotenv()

ADMIN_USERNAME = os.getenv('DB_USERNAME')
ADMIN_PASSWORD = os.getenv('DB_PASSWORD')
DB_SERVER = os.getenv('DB_SERVER_URL')
DATABASE_NAME = os.getenv('DB_NAME')

if all([ADMIN_USERNAME, ADMIN_PASSWORD, DB_SERVER, DATABASE_NAME]):
    DB_URL = f'mysql+pymysql://{ADMIN_USERNAME}:{ADMIN_PASSWORD}@{DB_SERVER}/{DATABASE_NAME}' 

else:
    DB_URL = None

# ----------------------------------------------------

JWT_SECRET = os.getenv('SECRET_KEY', default="my-default-secret-key-1234567890")
JWT_ALGORITHM = os.getenv('ALGORITHM', default="HS256")

# ----------------------------------------------------
