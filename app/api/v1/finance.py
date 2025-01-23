from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_finances():
    return {"message": "List of finances"}
