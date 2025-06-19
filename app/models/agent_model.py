# app/models/agent_model.py

from bson import ObjectId
from app.utils.db import db
from datetime import datetime

def create_agent(data: dict) -> str:
    data["created_at"] = datetime.utcnow()
    result = db.agents.insert_one(data)
    return str(result.inserted_id)

def get_agent_by_id(agent_id: str):
    return db.agents.find_one({"_id": ObjectId(agent_id)})

def get_agent_stats(agent_id: str):
    agent_id_obj = ObjectId(agent_id) if isinstance(agent_id, str) else agent_id
    listings = db.properties.count_documents({"agent_id": agent_id_obj})
    sold = db.properties.count_documents({"agent_id": agent_id_obj, "status": "sold"})
    reviews = db.reviews.count_documents({"agent_id": agent_id_obj})
    return {"listings": listings, "sold": sold, "reviews": reviews}

def get_agent_listings(agent_id: str):
    agent_id_obj = ObjectId(agent_id) if isinstance(agent_id, str) else agent_id
    return list(db.properties.find({"agent_id": agent_id_obj, "status": "listed"}))

def get_agent_sold(agent_id: str):
    agent_id_obj = ObjectId(agent_id) if isinstance(agent_id, str) else agent_id
    return list(db.properties.find({"agent_id": agent_id_obj, "status": "sold"}))

def serialize_agent(agent: dict):
    if not agent:
        return None
    return {
        "id": str(agent["_id"]),
        "name": agent.get("name"),
        "email": agent.get("email"),
        "profile_image_url": agent.get("profile_image_url"),
        "created_at": agent.get("created_at")
    }
