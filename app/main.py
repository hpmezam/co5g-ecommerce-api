from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database.session import init_db

from app.database import base  
from app.routes import auth, product

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="CO5G-ECOMMERCE-API",
    lifespan=lifespan,
    swagger_ui_parameters={
        "persistAuthorization": True
    }
)

app.include_router(auth)
app.include_router(product)