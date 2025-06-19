from fastapi import APIRouter, HTTPException
from app.controllers import booking_controller
from app.schemas.booking_schema import BookingCreate, BookingStatusUpdate
from typing import List

router = APIRouter(prefix="/api", tags=["Bookings"])

@router.post("/bookings", status_code=201)
def create_booking(data: BookingCreate):
    booking_id = booking_controller.create_booking(data.dict())
    return {"message": "Booking created", "id": booking_id}

@router.get("/bookings/{booking_id}")
def get_booking(booking_id: str):
    booking = booking_controller.fetch_booking_detail(booking_id)
    if booking:
        return booking
    raise HTTPException(status_code=404, detail="Booking not found")

@router.get("/properties/{property_id}/bookings")
def get_bookings_by_property(property_id: str):
    return booking_controller.fetch_bookings_by_property_id(property_id)

@router.get("/agents/{agent_id}/bookings")
def get_bookings_by_agent(agent_id: str):
    return booking_controller.fetch_bookings_by_agent_id(agent_id)

@router.put("/bookings/{booking_id}/status")
def update_booking(booking_id: str, data: BookingStatusUpdate):
    if booking_controller.update_booking_status(booking_id, data.status):
        return {"message": "Booking status updated"}
    raise HTTPException(status_code=404, detail="Booking not found")
