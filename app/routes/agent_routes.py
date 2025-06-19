from fastapi import APIRouter, HTTPException
from app.controllers import agent_controller
from app.schemas.agent_schema import AgentCreate

router = APIRouter(prefix="/api/agents", tags=["Agents"])

@router.post("/", status_code=201)
def create_agent(data: AgentCreate):
    agent_id = agent_controller.create_agent(data.dict())
    return {"message": "Agent created", "id": agent_id}

@router.get("/{agent_id}")
def get_agent(agent_id: str):
    agent = agent_controller.get_agent_profile(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@router.get("/{agent_id}/listings")
def get_agent_listings(agent_id: str):
    return agent_controller.get_agent_listings(agent_id)

@router.get("/{agent_id}/sold")
def get_agent_sold(agent_id: str):
    return agent_controller.get_agent_sold(agent_id)
