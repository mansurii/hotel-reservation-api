from pydantic import BaseModel
from typing import Literal, Optional

class Room(BaseModel):
    room_number: int
    room_type: Literal["Single", "Double", "Suite"]
    price: float
    status: Literal["available", "occupied"]

class RoomPartialUpdate(BaseModel):
    room_type: Optional[Literal["Single", "Double", "Suite"]] = None
    price: Optional[float] = None
    status: Optional[Literal["available", "occupied"]] = None

class RoomUpdate(BaseModel):
    room_type: Literal["Single", "Double", "Suite"]
    price: float
    status: Literal["available", "occupied"]

class GuestCreate(BaseModel):
    name: str
    email: str
    phone: str

class GuessUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class Guest(BaseModel):
    guest_id: int
    name: str
    email: str
    phone: str

class CreateBooking(BaseModel):
    guest: Guest
    room: Room
