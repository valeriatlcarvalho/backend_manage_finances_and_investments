from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
def get_users():
    return {"message": "List of users"}

@router.post("/")
def create_user(user: dict):
    if not user.get("email"):
        raise HTTPException(status_code=400, detail="Email is required")
    return {"message": "User created", "user": user}
