from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from datetime import datetime

class ReelBase(BaseModel):
    title: str = Field(..., example="Villa Tour")
    description: Optional[str] = Field(None, example="Check out this villa")
    video_url: HttpUrl = Field(..., example="http://example.com/video.mp4")
    property_id: str = Field(..., example="6657a1cf7b3f4e0123456789")
    location: Optional[str] = Field(None, example="Chennai, India")  # 🔧 optional now

class ReelCreate(ReelBase):
    pass

class ReelResponse(ReelBase):
    id: str
    likes: int = 0
    dislikes: int = 0
    shares: int = 0
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
