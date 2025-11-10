from database import engine
from fastapi import FastAPI
from routes import user
import modelus

modelus.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(user.router)




