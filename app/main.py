from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database.session import init_db

from app.database import base  
from app.routes import auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth)