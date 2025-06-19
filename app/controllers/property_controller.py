# app/controllers/property_controller.py

from app.models import property_model

def create_new_property(data: dict):
    return property_model.insert_property(data)

def fetch_all_properties():
    return property_model.get_all_properties()

def fetch_property_detail(property_id: str):
    return property_model.get_property_by_id(property_id)

def fetch_properties_by_agent_id(agent_id: str):
    return property_model.get_properties_by_agent_id(agent_id)
