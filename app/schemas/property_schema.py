from pydantic import BaseModel, Field
from typing import List, Optional

class GeoLocation(BaseModel):
    type: str = Field(..., example="Point")  # should be "Point"
    coordinates: List[float]  # [longitude, latitude]

class PropertyCreate(BaseModel):
    name: str
    type: str  # e.g., "House", "Apartment", etc.
    location: GeoLocation
    address: str
    rating: Optional[float] = 0
    city: str
    country: str
    image_url: str
    agent_id: str
