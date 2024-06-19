from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, models, utils, schemas, oauth2

router = APIRouter()

@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(database.get_db)):
    # print("user credentials: ",user_credentials)
    user = db.query(models.User).filter(models.User.email==user_credentials.username).first()
    print('username: ',user_credentials.username)
    print(user.id)
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    access_token = oauth2.create_access_token(data = {"user_id":user.id})

    return {"access_token":access_token, "token_type":"bearer"}