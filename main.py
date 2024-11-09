from sqlmodel import Session, select
from models import engine, Snack, Room, Snack_BaseModel, Order_Model
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/snacks", response_model=List[Snack])
def get_snacks():
    with Session(engine) as session:
        statement = select(Snack)
        results = session.exec(statement).all()
        return results


@app.post("/snack", response_model=Snack)
async def add_snacks(snack: Snack_BaseModel):
    with Session(engine) as session:
        new_snack = Snack(name=snack.name, price=snack.price, image_url=snack.image_url)
        session.add(new_snack)
        session.commit()
        session.refresh(new_snack)
    return new_snack


@app.get("/rooms", response_model=List[Room])
async def get_rooms():
    with Session(engine) as session:
        statement = select(Room)
        results = session.exec(statement).all()
        return results


@app.post("/order")
async def on_order(order: Order_Model):
    print("🛒 cart => ", order.cart)
    print("🚪 room_number_string => ", order.room_number_string)
    return Response(status_code=200)
