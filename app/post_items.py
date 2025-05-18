from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

items = []

class Item(BaseModel):
    item: str

@router.post("/items")
def store_item(data: Item):
    items.append(data.item)
    return {
        "success": True,
        "data": items,
        "message": "Data stored successfully",
    }
