from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class BookingCreate(BaseModel):
    property_id: str = Field(..., description="ID of the property being booked")
    agent_id: str = Field(..., description="ID of the agent handling the booking")
    user_id: Optional[str] = Field(None, description="ID of the user making the booking")
    date: datetime = Field(..., description="Date of the booking")

    class Config:
        from_attributes = True


class BookingStatusUpdate(BaseModel):
    status: str = Field(..., description="Updated booking status (e.g., pending, confirmed, cancelled)")

    class Config:
        from_attributes = True


class BookingResponse(BaseModel):
    id: str
    property_id: str
    agent_id: str
    user_id: Optional[str]
    status: str
    date: datetime
    created_at: datetime

    class Config:
        from_attributes = True
