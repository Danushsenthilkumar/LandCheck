from fastapi import APIRouter, HTTPException
from app.controllers import reel_controller
from app.schemas.reel_schema import ReelCreate
from typing import List

router = APIRouter(prefix="/api/reels", tags=["Reels"])

@router.post("/", status_code=201)
def create_reel(data: ReelCreate):
    """Create a new reel."""
    reel_id = reel_controller.create_new_reel(data.dict())
    return {"message": "Reel created", "id": reel_id}

@router.get("/")
def get_reels():
    """Fetch all reels."""
    return reel_controller.fetch_all_reels()

@router.get("/{reel_id}")
def get_reel(reel_id: str):
    """Fetch reel by ID."""
    reel = reel_controller.fetch_reel_detail(reel_id)
    if not reel:
        raise HTTPException(status_code=404, detail="Reel not found")
    return reel

@router.post("/{reel_id}/like")
def like_reel(reel_id: str):
    """Add like to a reel."""
    if reel_controller.add_like(reel_id):
        return {"message": "Reel liked"}
    raise HTTPException(status_code=404, detail="Reel not found")

@router.post("/{reel_id}/dislike")
def dislike_reel(reel_id: str):
    """Add dislike to a reel."""
    if reel_controller.add_dislike(reel_id):
        return {"message": "Reel disliked"}
    raise HTTPException(status_code=404, detail="Reel not found")

@router.post("/{reel_id}/share")
def share_reel(reel_id: str):
    """Add share to a reel."""
    if reel_controller.add_share(reel_id):
        return {"message": "Reel shared"}
    raise HTTPException(status_code=404, detail="Reel not found")
