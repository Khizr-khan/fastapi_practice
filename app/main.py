from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import post, user, auth, votes
from . import models
from .config import Settings 

from .database import engine

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers = ['*']
)

# settings = Settings()
# settings = Settings(_env_file='.env', _env_file_encoding='utf-8')

# print(settings.access_token_expire_minutes)


# models.Base.metadata.create_all(bind = engine) We doesn't need this statement now after we are using alembic






app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {"message": "Hello World"}
