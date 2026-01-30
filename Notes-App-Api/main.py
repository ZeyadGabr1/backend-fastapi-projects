from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from databse_settings import models
from databse_settings.settings import engine
from api.v1.routes import notes, auth

app = FastAPI()
models.Base.metadata.create_all(engine)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(notes.router)
app.include_router(auth.router)