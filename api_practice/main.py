from fastapi import FastAPI, HTTPException, status, Response, Depends
from pydantic import BaseModel
from typing import Optional

# from database import engine
from . import models
from .database import get_db, engine
from sqlalchemy.orm import Session
from .schemas import Item_Create, City_Out, City
from .routers import users, cities, auth
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_password: str = 'localhost'
    database_username: str = 'postgres'
    secret_key: str = "234ui2340892348"

settings = Settings()

print(settings.database_username)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(cities.router)
app.include_router(auth.router)