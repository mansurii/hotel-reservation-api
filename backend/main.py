from fastapi import FastAPI

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
            "name": "James Wilson",
            "email": "james@example.com",
            "phone": "+44 7700 900001"
        },
        {
            "name": "Aisha Khan",
            "email": "aisha@example.com",
            "phone": "+44 7700 900002"
        },
        {
            "name": "Daniel Brown",
            "email": "daniel@example.com",
            "phone": "+44 7700 900003"
        },
        {
            "name": "Sophia Taylor",
            "email": "sophia@example.com",
            "phone": "+44 7700 900004"
        }
    ],

    "bookings": [
        {
            "booking_id": 1,
            "guest": {
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
async def create_room():
    pass

@app.get("/rooms")
async def get_rooms():
    pass

@app.post("/guests")
async def create_guest():
    pass

@app.get("/guests")
async def get_guests():
    pass


@app.post("/bookings")
async def create_booking():
    pass

@app.get("/bookings")
async def get_bookings():
    pass

@app.patch("/bookings/{booking_id}/checkout")
async def checkout_cancel_bookings(booking_id: int):
    pass