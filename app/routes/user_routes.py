from fastapi import APIRouter, HTTPException
from app.controllers import user_controller
from app.schemas.user_schema import UserCreate

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.post("/", status_code=201)
def create_user(data: UserCreate):
    """Create a new user."""
    user_id = user_controller.create_user(data.dict())
    return {"message": "User created", "id": user_id}

@router.get("/{user_id}")
def get_user(user_id: str):
    """Get user by user_id."""
    user = user_controller.fetch_user_detail(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/email/{email}")
def get_user_by_email(email: str):
    """Get user by email."""
    user = user_controller.fetch_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
