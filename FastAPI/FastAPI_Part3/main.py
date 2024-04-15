from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr, validator, constr
from typing import Optional, List
from datetime import datetime

from starlette.responses import HTMLResponse

app = FastAPI()

# Simulated database for demonstration
database_usernames = set()  # This set will store usernames to simulate a user database.
database_items = {}  # This dictionary will simulate an item database by item_id.


class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    state: str
    country: str
    zip_code: str


class User(BaseModel):
    id: int
    username: str
    name: str = Field(..., example="John Doe", min_length=2, max_length=50)
    age: int = Field(ge=18, le=100, description="Age must be between 18 and 100.")
    email: EmailStr = Field(description="Email address of the user.")
    bio: Optional[str] = Field(None, max_length=300, description="A brief biography of the user.")
    address: Address  # Nested model

    @validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('Name must contain a space')
        return v.title()

    @validator('age')
    def validate_age(cls, v):
        if v < 18:
            raise ValueError('User must be at least 18 years old')
        return v


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


@app.post("/users/", response_model=User)
async def create_user(user: User):
    if user.username in database_usernames:
        raise HTTPException(status_code=400, detail="Username already registered")
    database_usernames.add(user.username)  # Add username to the simulated database
    return user


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id not in database_items:
        raise HTTPException(status_code=404, detail="Item not found")
    return database_items[item_id]


@app.get("/", response_class=HTMLResponse)
async def welcome():
    html_content = """
    <html>
        <head>
            <title>API Usage</title>
            <style>
                body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
                h1 { color: #333; }
                ul { list-style-type: none; padding: 0; }
                li { margin: 10px 0; }
                code { background: #f4f4f4; padding: 2px 6px; }
            </style>
        </head>
        <body>
            <h1>Welcome to Our API!</h1>
            <p>Here are some instructions on how to use this API:</p>
            <ul>
                <li>
                    <strong>POST</strong> - Create a new user. Requires a unique username.<br>
                    Endpoint: <code>/users/</code>
                </li>
                <li>
                    <strong>GET</strong> - Retrieve item details by item ID.<br>
                    Endpoint: <code>/items/{item_id}</code>
                </li>
            </ul>
            <h2>Example Endpoints:</h2>
            <ul>
                <li>Create User: <code>/users/</code></li>
                <li>Read Item: <code>/items/1</code></li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


database_items[1] = Item(id=1, name="Widget", description="A useful widget", price=15.99)
database_items[2] = Item(id=2, name="Gadget", description="An essential gadget", price=23.50)
# Running the API with Uvicorn. This command should be in a separate runner file or in the command line.
# `uvicorn main:app --reload` where `main` is the name of your Python file.
