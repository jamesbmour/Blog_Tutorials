from typing import Optional

from fastapi import FastAPI

app = FastAPI()

# Basic routing with an HTTP GET method to return a welcome message
@app.get("/")
async def home():
    return {"message": "Welcome to our API!"}

@app.post("/items/", status_code=status.HTTP_201_CREATED, tags=["Item Operations"])
async def create_item(item: Item):
    """
    Create an item in the database.
    """
    db.add(item)
    return item

# Defining a route that captures a path parameter
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # FastAPI automatically validates and converts `user_id` to an integer
    return {"user_id": user_id}

@app.get("/items/{category_id}/products/{product_id}")
async def get_product(category_id: int, product_id: int):
    return {"category_id": category_id, "product_id": product_id}

# Defining a route that uses query parameters to filter data (e.g., for pagination)
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10, search: Optional[str] = None):
    items = fetch_items(skip=skip, limit=limit, search_query=search)
    return {"items": items, "skip": skip, "limit": limit}

# Running the API with Uvicorn. This command should be in a separate runner file or in the command line.
# `uvicorn main:app --reload` where `main` is the name of your Python file.
