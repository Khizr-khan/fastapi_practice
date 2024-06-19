from api_practice import models, schemas, oauth2
from fastapi import FastAPI,Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from ..database import engine, get_db

router = APIRouter()


@router.get("/items/{item_id}", response_model=List[schemas.City_Out])
def read_item(item_id:int, db: Session = Depends(get_db)):
    # items = find_id(item_id)
    # print('item_id: ',item_id)
    item_query = db.query(models.City).filter(models.City.id==item_id).all()
    # print(item_query)
    return item_query

@router.get("/items", response_model=List[schemas.City_Out])
def read_item(db: Session = Depends(get_db)):
    
    
    item_query = db.query(models.City).all()
    # print('-----------------------------')
    # print(item_query)
    # print(item_query)
    return item_query

@router.post("/items", status_code=status.HTTP_201_CREATED, response_model=schemas.City_Out)
def create_item(item: schemas.Item_Create, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    # print('item: ',item)
    print('current_user_id: ',current_user.id)
    new_item = models.City(owner_id = current_user.id, **item.dict())
    # print(new_item)
    print('new item: ',new_item)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)  # the refresh will help in return the item in return statement
    return new_item
