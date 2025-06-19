# app/models/reel_model.py

from app.utils.db import db
from bson import ObjectId
from datetime import datetime

def insert_reel(data: dict) -> str:
    data["created_at"] = datetime.utcnow()
    data["likes"] = 0
    data["dislikes"] = 0
    data["shares"] = 0

    # 💡 Convert HttpUrl to str just to be safe
    if "video_url" in data:
        data["video_url"] = str(data["video_url"])

    result = db.reels.insert_one(data)
    return str(result.inserted_id)


def get_all_reels():
    reels = db.reels.find()
    return [serialize_reel(r) for r in reels]

def get_reel_by_id(reel_id: str):
    return serialize_reel(db.reels.find_one({"_id": ObjectId(reel_id)}))

def like_reel(reel_id: str):
    return db.reels.update_one({"_id": ObjectId(reel_id)}, {"$inc": {"likes": 1}})

def dislike_reel(reel_id: str):
    return db.reels.update_one({"_id": ObjectId(reel_id)}, {"$inc": {"dislikes": 1}})

def share_reel(reel_id: str):
    return db.reels.update_one({"_id": ObjectId(reel_id)}, {"$inc": {"shares": 1}})

def serialize_reel(reel: dict):
    if not reel:
        return None
    return {
        "id": str(reel["_id"]),
        "title": reel.get("title"),
        "location": reel.get("location"),
        "rating": reel.get("rating"),
        "video_url": reel.get("video_url"),
        "likes": reel.get("likes", 0),
        "dislikes": reel.get("dislikes", 0),
        "shares": reel.get("shares", 0),
        "created_at": reel.get("created_at")
    }
