# app/models/property_model.py

from app.utils.db import db
from bson import ObjectId
from datetime import datetime

def insert_property(data: dict) -> str:
    data["created_at"] = datetime.utcnow()

    if "agent_id" in data and isinstance(data["agent_id"], str):
        data["agent_id"] = ObjectId(data["agent_id"])

    result = db.properties.insert_one(data)
    return str(result.inserted_id)

def get_all_properties():
    properties = db.properties.find()
    return [serialize_property(p) for p in properties]

def get_property_by_id(property_id: str):
    prop = db.properties.find_one({"_id": ObjectId(property_id)})
    return serialize_property(prop)

def get_properties_by_agent_id(agent_id: str):
    agent_id_obj = ObjectId(agent_id) if isinstance(agent_id, str) else agent_id
    properties = db.properties.find({"agent_id": agent_id_obj})
    return [serialize_property(p) for p in properties]

def serialize_property(prop: dict):
    if not prop:
        return None
    return {
        "id": str(prop["_id"]),
        "name": prop.get("name"),
        "type": prop.get("type"),
        "location": prop.get("location"),
        "address": prop.get("address"),
        "rating": prop.get("rating"),
        "city": prop.get("city"),
        "country": prop.get("country"),
        "image_url": prop.get("image_url"),
        "created_at": prop.get("created_at"),
        "agent_id": str(prop.get("agent_id")) if prop.get("agent_id") else None
    }
