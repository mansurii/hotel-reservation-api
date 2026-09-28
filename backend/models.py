from pydantic import BaseModel
from typing import Literal

class Room(BaseModel):
    room_number: int
    room_type: Literal["Single", "Double", "Suite"]
    price: float
    status: Literal["available", "occupied"]

class Guest(BaseModel):
    name: str
    email: str
    phone: str

class Book(BaseModel):
    booking_id: int
    guest: Guest
    room: Room
    status: Literal["check_in", "check_out"]

