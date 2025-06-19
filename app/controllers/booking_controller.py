# app/controllers/booking_controller.py

from app.models import booking_model

def create_booking(data):
    return booking_model.create_booking(data)

def fetch_booking_detail(booking_id):
    booking = booking_model.get_booking_by_id(booking_id)
    return booking_model.serialize_booking(booking)

def fetch_bookings_by_property_id(property_id):
    bookings = booking_model.get_bookings_by_property_id(property_id)
    return [booking_model.serialize_booking(b) for b in bookings]

def fetch_bookings_by_agent_id(agent_id):
    bookings = booking_model.get_bookings_by_agent_id(agent_id)
    return [booking_model.serialize_booking(b) for b in bookings]

def update_booking_status(booking_id, status):
    return booking_model.update_booking_status(booking_id, status)
