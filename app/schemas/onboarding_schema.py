from pydantic import BaseModel, Field
from typing import List, Optional


class OnboardingData(BaseModel):
    preferred_locations: Optional[List[str]] = Field(default_factory=list)
    property_types: Optional[List[str]] = Field(default_factory=list)
    budget_range: Optional[List[int]] = Field(default_factory=list, min_items=2, max_items=2)
    important_amenities: Optional[List[str]] = Field(default_factory=list)
    lifestyle_preferences: Optional[List[str]] = Field(default_factory=list)

    class Config:
        from_attributes = True  # replaces orm_mode in Pydantic v2+
