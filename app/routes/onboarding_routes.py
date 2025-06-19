from fastapi import APIRouter, Header, HTTPException, Depends
from app.schemas.onboarding_schema import OnboardingData
from app.models import onboarding_model

router = APIRouter(prefix="/api/onboarding", tags=["Onboarding"])

@router.post("/")
def save_onboarding(
    data: OnboardingData,
    user_id: str = Header(..., alias="user_id")  # 👈 explicitly define alias
):
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized: Missing user_id in headers")
    
    onboarding_model.save_or_update_onboarding(user_id, data.dict())
    return {"message": "Onboarding saved successfully"}
