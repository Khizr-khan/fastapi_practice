from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class Item_Create(BaseModel):
    name: str
    price: float
    tax: Optional[float] = None 

class City(Item_Create):
    pass

class City_Out(Item_Create):
    id: int

    class config:
        from_attributes = True
    
class UserOut(BaseModel):
    email: EmailStr
    id: int
    created_at: datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    class config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

"""
{
    "email":"monank@gmail.com",
    "password":"qwerty1234"
}

{
    "email":"khank@gmail.com",
    "password":"asdfg1234"
}

"""