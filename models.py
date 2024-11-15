from sqlmodel import SQLModel, Field, create_engine, Session, select
from pydantic import BaseModel
from typing import List


class Snack(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: float
    image_url: str


class Room(SQLModel, table=True):
    number_string: str = Field(default=None, primary_key=True)  # A317
    floor: int  # 3


class Snack_BaseModel(BaseModel):
    id: int
    name: str
    price: float
    image_url: str
    quantity : int


class Order_Model(BaseModel):
    cart: List[Snack_BaseModel]  # 购物车
    room_number_string: str  # 房间号


class SnacksCartModdel(BaseModel):
    name: str = Field(min_length=3, max_length=50)


DATABASE_URL = "sqlite:///./data.db"
engine = create_engine(DATABASE_URL, echo=False)

SQLModel.metadata.create_all(engine)
