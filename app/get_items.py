from fastapi import APIRouter

router = APIRouter()

items = ['Apple', 'Banana']

@router.get("/items")
def get_items():
    return {
        "success": True,
        "data": items,
        "message": "Data fetched successfully",
    }
