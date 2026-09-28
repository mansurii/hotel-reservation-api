from fastapi import FastAPI
app = FastAPI()

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