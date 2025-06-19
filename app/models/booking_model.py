# app/models/booking_model.py

from app.utils.db import db
from bson import ObjectId
from datetime import datetime

def create_booking(data: dict) -> str:
    data["created_at"] = datetime.utcnow()
    data["status"] = "pending"  # initial booking status
    result = db.bookings.insert_one(data)
    return str(result.inserted_id)

def get_booking_by_id(booking_id: str):
    return db.bookings.find_one({"_id": ObjectId(booking_id)})

def get_bookings_by_property_id(property_id: str):
    return list(db.bookings.find({"property_id": ObjectId(property_id)}))

def get_bookings_by_agent_id(agent_id: str):
    return list(db.bookings.find({"agent_id": ObjectId(agent_id)}))

def update_booking_status(booking_id: str, status: str) -> bool:
    result = db.bookings.update_one(
        {"_id": ObjectId(booking_id)},
        {"$set": {"status": status}}
    )
    return result.modified_count > 0

def serialize_booking(booking: dict):
    if not booking:
        return None
    return {
        "id": str(booking["_id"]),
        "property_id": str(booking["property_id"]),
        "agent_id": str(booking["agent_id"]),
        "user_id": str(booking.get("user_id")),
        "status": booking.get("status"),
        "date": booking.get("date"),
        "created_at": booking.get("created_at")
    }
