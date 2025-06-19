# app/controllers/agent_controller.py

from app.models import agent_model, property_model

def create_agent(data):
    # Ensure serializable types (e.g., convert HttpUrl to str if needed)
    if "profile_image_url" in data:
        data["profile_image_url"] = str(data["profile_image_url"])
    return agent_model.create_agent(data)


def get_agent_profile(agent_id: str):
    agent = agent_model.get_agent_by_id(agent_id)
    if not agent:
        return None

    stats = agent_model.get_agent_stats(agent_id)

    return {
        "id": str(agent.get("_id")),
        "name": agent.get("name"),
        "email": agent.get("email"),
        "profile_image_url": str(agent.get("profile_image_url")),
        "stats": stats,
    }


def get_agent_listings(agent_id: str):
    listings = agent_model.get_agent_listings(agent_id)

    return [map_property_summary(p) for p in listings]


def get_agent_sold(agent_id: str):
    sold = agent_model.get_agent_sold(agent_id)

    return [map_property_summary(p) for p in sold]


def map_property_summary(p):
    return {
        "id": str(p["_id"]),
        "name": p.get("name"),
        "price": p.get("price"),
        "image_url": str(p.get("image_url")) if p.get("image_url") else None,
        "rating": p.get("rating", 0),
        "city": p.get("city"),
        "country": p.get("country"),
    }
