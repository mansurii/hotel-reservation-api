from fastapi import FastAPI
from fastapi import HTTPException
from models import Room, Guest, Book
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

@app.post("/guests")
async def create_guest(guest: Guest):
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


@app.post("/bookings")
async def create_booking(new_booking: Book):
    guess_found = None

    for guess in db_guests:
        if guess["guest_id"] == new_booking.guest.guest_id:
            guess_found = guess
            break

    if guess_found is None:
        raise HTTPException(status_code=404, detail="Guess not found")

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
        "guess": guess_found,
        "room": room_found,
        "status": "check_in"
    }

    db_bookings.append(new_booking)

    room_found["status"] = "occupied"

    new_booking["room"]["status"] = "occupied"

    return new_booking

@app.get("/bookings")
async def get_bookings():
    return db_bookings

@app.patch("/bookings/{booking_id}/checkout")
async def checkout_cancel_bookings(booking_id: int):
    pass