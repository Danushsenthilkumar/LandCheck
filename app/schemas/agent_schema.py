from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import Optional
from datetime import datetime

class AgentCreate(BaseModel):
    name: str = Field(..., example="John Doe")
    email: EmailStr = Field(..., example="johndoe@example.com")
    profile_image_url: Optional[HttpUrl] = Field(None, example="https://example.com/profile.jpg")

class AgentOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    profile_image_url: Optional[HttpUrl]
    created_at: datetime
