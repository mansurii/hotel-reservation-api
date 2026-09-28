from pydantic import BaseModel
from typing import Literal

class Room(BaseModel):
    room_number: int
    room_type: Literal["Single", "Double", "Suite"]
    price: float
    status: Literal["available", "occupied"]

class GuestCreate(BaseModel):
    name: str
    email: str
    phone: str

class Guest(BaseModel):
    guest_id: int
    name: str
    email: str
    phone: str

class Booking(BaseModel):
    guest: Guest
    room: Room

