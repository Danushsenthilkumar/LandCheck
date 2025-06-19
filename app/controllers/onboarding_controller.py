# app/controllers/onboarding_controller.py

from app.models import onboarding_model

def save_onboarding_data(user_id: str, data: dict):
    onboarding_model.save_or_update_onboarding(user_id, data)
    return {"message": "Onboarding data saved successfully"}
