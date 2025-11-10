from fastapi import FastAPI
from db import models
from db import connection
from routes import user, products, orders
from auth import authentecator


models.Base.metadata.create_all(connection.connection.engine)

app = FastAPI()


app.include_router(authentecator.router)
app.include_router(user.router)
app.include_router(products.router)
app.include_router(orders.router)


