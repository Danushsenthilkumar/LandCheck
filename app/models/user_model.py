from app.utils.db import db  # ✅ Correct import
from bson import ObjectId
from datetime import datetime

def create_user(data):
    data["created_at"] = datetime.utcnow()
    result = db.users.insert_one(data)
    return str(result.inserted_id)

def get_user_by_id(user_id):
    return db.users.find_one({"_id": ObjectId(user_id)})

def get_user_by_email(email):
    return db.users.find_one({"email": email})

def serialize_user(user):
    if not user:
        return None
    return {
        "id": str(user["_id"]),
        "name": user.get("name"),
        "email": user.get("email"),
        "phone": user.get("phone"),  # ✅ Safe
        "created_at": user.get("created_at")
    }
