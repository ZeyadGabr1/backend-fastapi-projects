from fastapi import FastAPI
from db import models
from db.connection import engine
from routes import user, task
from auth  import authentecator

app = FastAPI()

models.Base.metadata.create_all(engine)

# -------------------------------------
app.include_router(user.router)
app.include_router(task.router)
app.include_router(authentecator.router)
# -------------------------------------
