# app/controllers/reel_controller.py

from app.models import reel_model

def create_new_reel(data: dict):
    return reel_model.insert_reel(data)

def fetch_all_reels():
    return reel_model.get_all_reels()

def fetch_reel_detail(reel_id: str):
    return reel_model.get_reel_by_id(reel_id)

def add_like(reel_id: str):
    result = reel_model.like_reel(reel_id)
    return result.modified_count > 0

def add_dislike(reel_id: str):
    result = reel_model.dislike_reel(reel_id)
    return result.modified_count > 0

def add_share(reel_id: str):
    result = reel_model.share_reel(reel_id)
    return result.modified_count > 0
