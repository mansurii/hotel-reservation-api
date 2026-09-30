from fastapi import FastAPI
from fastapi import HTTPException
from models import Room, CreateBooking, GuestCreate, GuestUpdate, GuestPartialUpdate, RoomPartialUpdate, RoomUpdate

app = FastAPI(title="Hotel Reservation API")

# Create fake database with prepopulated data
database = {
    "rooms": [
        {
            "room_number": 1,
            "room_type": "Single",
            "price": 80.0,
            "status": "available"
        },
        {
            "room_number": 2,
            "room_type": "Double",
            "price": 120.0,
            "status": "occupied"
        },
        {
            "room_number": 3,
            "room_type": "Suite",
            "price": 200.0,
            "status": "available"
        },
        {
            "room_number": 4,
            "room_type": "Double",
            "price": 130.0,
            "status": "available"
        }
    ],

    "guests": [
        {
            "guest_id": 1,
            "name": "James Wilson",
            "email": "james@example.com",
            "phone": "+44 7700 900001"
        },
        {
            "guest_id": 2,
            "name": "Aisha Khan",
            "email": "aisha@example.com",
            "phone": "+44 7700 900002"
        },
        {
            "guest_id": 3,
            "name": "Daniel Brown",
            "email": "daniel@example.com",
            "phone": "+44 7700 900003"
        },
        {
            "guest_id": 4,
            "name": "Sophia Taylor",
            "email": "sophia@example.com",
            "phone": "+44 7700 900004"
        }
    ],

    "bookings": [
        {
            "booking_id": 1,
            "guest": {
                "guest_id": 1,
                "name": "James Wilson",
                "email": "james@example.com",
                "phone": "+44 7700 900001"
            },
            "room": {
                "room_number": 2,
                "room_type": "Double",
                "price": 120.0,
                "status": "occupied"
            },
            "status": "check_in"
        },
        {
            "booking_id": 2,
            "guest": {
                "guest_id": 2,
                "name": "Aisha Khan",
                "email": "aisha@example.com",
                "phone": "+44 7700 900002"
            },
            "room": {
                "room_number": 3,
                "room_type": "Suite",
                "price": 200.0,
                "status": "available"
            },
            "status": "check_out"
        }
    ]
}

db_rooms = database["rooms"]
db_guests = database["guests"]
db_bookings = database["bookings"]

@app.post("/rooms")
async def create_room(room: Room):
    for check_room_exist in db_rooms:
        if check_room_exist["room_number"] == room.room_number:
            raise HTTPException(status_code=409, detail="Room already exists")

    new_room = {
        "room_number": room.room_number,
        "room_type": room.room_type,
        "price": room.price,
        "status": room.status
    }

    db_rooms.append(new_room)

    return new_room

@app.get("/rooms")
async def get_rooms():
    return db_rooms

@app.delete("/rooms/{room_number}")
async  def delete_room(room_number: int):
    room_found = None

    for room in db_rooms:
        if room["room_number"] == room_number:
            room_found = room
            break
    if room_found is None:
        raise HTTPException(status_code=404, detail="Room not found")

    if room_found["status"] == "occupied":
        raise HTTPException(status_code=409, detail="Cannot delete an occupied room")

    db_rooms.remove(room_found)

    return { "message": "Room deleted successfully", "room": room_found}

@app.patch("/rooms/{room_number}")
async  def update_room_partial(room_number: int, updated_room_partial: RoomPartialUpdate):
    for room in db_rooms:
        if room["room_number"] == room_number:
            if updated_room_partial.room_type is not None:
                room["room_type"] = updated_room_partial.room_type
            if updated_room_partial.price is not None:
                room["price"] = updated_room_partial.price
            if updated_room_partial.status is not None:
                room["status"] = updated_room_partial.status
            return room
    raise HTTPException(status_code=404, detail="Room not found")

@app.put("/rooms/{room_number}")
async  def update_room(room_number: int, updated_room: RoomUpdate):
    for room in db_rooms:
        if room["room_number"] == room_number:
            room["room_type"] = updated_room.room_type
            room["price"] = updated_room.price
            room["status"] = updated_room.status
            return room
    raise HTTPException(status_code=404, detail="Room not found")

@app.get("/rooms/occupied")
async  def get_occupied_rooms():
    occupied_rooms = []
    for room in db_rooms:
        if room["status"] == "occupied":
            occupied_rooms.append(room)
    return occupied_rooms

@app.post("/guests")
async def create_guest(guest: GuestCreate):

    next_id = db_guests[-1]["guest_id"] + 1

    new_guest = {
        "guest_id": next_id,
        "name": guest.name,
        "email": guest.email,
        "phone": guest.phone
    }

    db_guests.append(new_guest)

    return new_guest

@app.get("/guests")
async def get_guests():
    return db_guests

@app.delete("/guests/{guest_id}")
async def delete_guest(guest_id: int):
    guest_found = None

    for guest in db_guests:
        if guest["guest_id"] == guest_id:
            guest_found = guest
            break

    if guest_found is None:
        raise HTTPException(status_code=404, detail="Guest not found")

    for booking in db_bookings:
        if (booking["guest"]["guest_id"] == guest_id
            and booking["status"] == "check_in"):
            raise HTTPException(status_code=409,detail="Cannot delete guest with an active booking")

    db_guests.remove(guest_found)

    return {"message": "Guest deleted successfully", "guest": guest_found}

@app.patch("/guests/{guest_id}")
async def update_guest_partial(guest_id: int, updated_guest_partial: GuestPartialUpdate):
    for guest in db_guests:
        if guest["guest_id"] == guest_id:
            if updated_guest_partial.name is not None:
                guest["name"] = updated_guest_partial.name
            if updated_guest_partial.email is not None:
                guest["email"] = updated_guest_partial.email
            if updated_guest_partial.phone is not None:
                guest["phone"] = updated_guest_partial.phone
            return  guest
    raise HTTPException(status_code=404, detail="Guest not found")

@app.put("/guests/{guest_id}")
async def update_guest(guest_id: int, updated_guest: GuestUpdate):
    for guest in db_guests:
        if guest["guest_id"] == guest_id:
            guest["name"] = updated_guest.name
            guest["email"] = updated_guest.email
            guest["phone"] = updated_guest.phone
            return guest
    raise HTTPException(status_code=404, detail="Guest not found")

async def create_booking(new_booking: CreateBooking):
    guest_found = None

    for guest in db_guests:
        if guest["guest_id"] == new_booking.guest.guest_id:
            guest_found= guest
            break

    if guest_found is None:
        raise HTTPException(status_code=404, detail="Guest not found")

    room_found = None

    for room in db_rooms:
        if room["room_number"] == new_booking.room.room_number:
            room_found = room
            break

    if room_found is None:
        raise HTTPException(status_code=404, detail="Room not found")

    if room_found["status"] != "available":
        raise HTTPException(status_code=409, detail="Room is not available")

    next_id = db_bookings[-1]["booking_id"] + 1

    new_booking = {
        "booking_id": next_id,
        "guest": guest_found,
        "room": room_found,
        "status": "check_in"
    }

    db_bookings.append(new_booking)

    room_found["status"] = "occupied"

    return new_booking

@app.get("/bookings")
async def get_bookings():
    return db_bookings

@app.patch("/bookings/{booking_id}/checkout")
async def checkout_bookings(booking_id: int):

    booking_found = None

    for booking in db_bookings:
        if booking["booking_id"] == booking_id:
            booking_found = booking
            break

    if booking_found is None:
        raise HTTPException(status_code=404, detail="Booking not found")

    if booking_found["status"] == "check_out":
        raise HTTPException(status_code=409, detail="Booking has already been checked out")

    room_number = booking_found["room"]["room_number"]

    room_found = None

    for room in db_rooms:
        if room["room_number"] == room_number:
            room_found = room
            break

    if room_found is None:
        raise HTTPException(status_code=404,detail="Room associated with booking not found")

    room_found["status"] = "available"

    booking_found["room"]["status"] = "available"

    booking_found["status"] = "check_out"

    return booking_found
