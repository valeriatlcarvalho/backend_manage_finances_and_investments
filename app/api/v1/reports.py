from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_reports():
    return {"message": "List of reports"}
