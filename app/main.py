from fastapi import FastAPI
from .get_items import router as get_items_router
from .post_items import router as post_items_router

app = FastAPI()

# Root page
@app.get('/')
def read_root():
    return {
        "success": True,
        "data": ["Welcome"],
        "message": "Hello World"
    }

# Include router from separate file
app.include_router(get_items_router)
app.include_router(post_items_router)
