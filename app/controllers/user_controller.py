# app/controllers/user_controller.py

from app.models import user_model

def create_user(data: dict):
    return user_model.create_user(data)

def fetch_user_detail(user_id: str):
    user = user_model.get_user_by_id(user_id)
    return user_model.serialize_user(user)

def fetch_user_by_email(email: str):
    user = user_model.get_user_by_email(email)
    return user_model.serialize_user(user)
