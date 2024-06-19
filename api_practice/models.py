from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, TIMESTAMP
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
import time
from typing import Optional


class User(Base):

    __tablename__ = "users"
    _table_args__ = {"existing":True}
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))


class City(Base):
    __tablename__ = "cities"
    _table_args__ = {"extend_existing":True}
    id = Column(Integer, primary_key=True, nullable = False)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    tax =  Column(Float, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("now()"))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)




'''
1	"Aligarh"	40000	5
2	"Rampur"	50000	6
3	"Moradabad"	20000	7
4	"Bangalore"	60000	8
6	"Delhi"	70000	8
'''