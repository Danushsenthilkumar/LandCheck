# app/models/onboarding_model.py

from app.utils.db import db

def save_or_update_onboarding(user_id: str, data: dict):
    existing = db.onboarding.find_one({"user_id": user_id})
    if existing:
        db.onboarding.update_one(
            {"user_id": user_id},
            {"$set": data}
        )
    else:
        data["user_id"] = user_id
        db.onboarding.insert_one(data)
