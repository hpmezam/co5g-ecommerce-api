from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database.session import init_db

from app.database import base  

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "API running with SQLAlchemy"}