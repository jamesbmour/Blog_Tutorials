from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import uuid4
from fastapi.responses import JSONResponse

app = FastAPI()

# In-memory database (list) for todos with some initial example items
todos = [
    {
        "id": str(uuid4()),
        "title": "Learn FastAPI",
        "description": "Go through the official FastAPI documentation and tutorials.",
        "completed": False,
        "created_at": datetime.now(),
    },
    {
        "id": str(uuid4()),
        "title": "Build a Todo API",
        "description": "Create a REST API for managing todo items using FastAPI.",
        "completed": False,
        "created_at": datetime.now(),
    },
    {
        "id": str(uuid4()),
        "title": "Write blog post",
        "description": "Draft a blog post about creating a Todo API with FastAPI.",
        "completed": False,
        "created_at": datetime.now(),
    },
]


# TodoCreate model for input validation
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


# Todo model for output
class Todo(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime


# Helper function to find a todo by ID
def get_todo_by_id(todo_id: str):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None


# Create a new todo
@app.post("/todos/", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo = Todo(
        id=str(uuid4()),
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        created_at=datetime.now()
    )
    todos.append(new_todo.dict())
    return new_todo


# Retrieve all todos
@app.get("/todos/", response_model=List[Todo])
def get_all_todos():
    return todos


# Retrieve a single todo by ID
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: str):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


# Update an existing todo
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: str, todo_data: TodoCreate):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo["title"] = todo_data.title
    todo["description"] = todo_data.description
    todo["completed"] = todo_data.completed
    return Todo(**todo)


# Delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos.remove(todo)
    return {"detail": "Todo deleted successfully"}


# ErrorResponse model for custom error responses
class ErrorResponse(BaseModel):
    detail: str


# Adding custom error response for not found errors
@app.exception_handler(HTTPException)
def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
