from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.controllers import property_controller
from app.models import property_model
from app.schemas.property_schema import PropertyCreate
from app.utils.db import db

router = APIRouter(prefix="/api/properties", tags=["Properties"])

@router.post("/", status_code=201)
def create_property(data: PropertyCreate):
    """Create a new property."""
    property_id = property_controller.create_new_property(data.dict())
    return {"message": "Property created", "id": property_id}

@router.get("/")
def get_properties():
    """Get a list of all properties."""
    return property_controller.fetch_all_properties()

@router.get("/nearby")
def get_nearby_properties(
    latitude: float = Query(...),
    longitude: float = Query(...),
    max_distance: int = Query(5000)
):
    """Get properties near a given latitude and longitude."""
    try:
        nearby = db.properties.find({
            "location": {
                "$near": {
                    "$geometry": {
                        "type": "Point",
                        "coordinates": [longitude, latitude]
                    },
                    "$maxDistance": max_distance
                }
            }
        })
        return [property_model.serialize_property(p) for p in nearby]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid coordinates or query: {e}")

@router.get("/search")
def search_properties(query: str = Query(...)):
    """Search properties by text (city, address, etc.)."""
    try:
        results = db.properties.find({
            "$text": { "$search": query }
        })
        return [property_model.serialize_property(p) for p in results]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Search failed: {e}")

@router.get("/{property_id}")  # ⬅️ MUST be last to prevent route conflict
def get_property(property_id: str):
    """Get property details by property_id."""
    prop = property_controller.fetch_property_detail(property_id)
    if not prop:
        raise HTTPException(status_code=404, detail="Property not found")
    return prop
