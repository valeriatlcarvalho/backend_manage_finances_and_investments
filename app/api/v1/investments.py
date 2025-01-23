from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_investments():
    return {"message": "List of investments"}
