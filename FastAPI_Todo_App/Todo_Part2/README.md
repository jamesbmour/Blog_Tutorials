# Building a Todo API with FastAPI: Step-by-Step Guide

## I. Introduction

In our previous post, we introduced FastAPI and set up a basic project structure. Now, we’ll take it a step further by building a functional Todo API. By the end of this tutorial, you’ll have a working backend that can create, read, update, and delete todo items.

### What We’ll Cover:
- Designing the Todo Data Model
- Implementing CRUD Operations
- Creating API Endpoints
- Adding Input Validation and Error Handling
- Testing the API
- Refactoring and Organizing Code

## II. Designing the Todo Data Model

To manage todos, we need to define a data model that represents a todo item. FastAPI uses Pydantic models to validate and parse data, so we’ll leverage that here.

### A. Defining the Todo Schema

We’ll create two models using Pydantic:
- **TodoCreate**: For input data when creating or updating a todo.
- **Todo**: For the complete todo item, including fields like `id` and `created_at`.

```python
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Todo(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime
```

### B. Explaining the Fields

- **id**: Unique identifier for each todo.
- **title**: Main content of the todo.
- **description**: Additional details (optional).
- **completed**: Boolean status of the todo (whether it's done or not).
- **created_at**: Timestamp indicating when the todo was created.

## III. Creating CRUD Operations for Todos

CRUD stands for Create, Read, Update, and Delete—the four basic operations for managing data. We’ll implement these operations using an in-memory database (a simple list) for this tutorial.

### A. Setting Up an In-Memory Database

We’ll use a list to store our todos. For simplicity, we’ll also add a few example todos.

```python
from uuid import uuid4
from datetime import datetime

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
```

### B. Implementing Helper Functions

We’ll implement a simple helper function to find a todo by its `id`.

```python
def get_todo_by_id(todo_id: str):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None
```

## IV. Implementing API Endpoints

### A. Creating a New Todo

The POST endpoint allows users to create a new todo item.

```python
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
```

### B. Retrieving All Todos

The GET endpoint retrieves all todos from our in-memory database.

```python
@app.get("/todos/", response_model=List[Todo])
def get_all_todos():
    return todos
```

### C. Retrieving a Single Todo

The GET endpoint allows retrieving a single todo by its `id`.

```python
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: str):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
```

### D. Updating a Todo

The PUT endpoint allows users to update an existing todo.

```python
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: str, todo_data: TodoCreate):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo["title"] = todo_data.title
    todo["description"] = todo_data.description
    todo["completed"] = todo_data.completed
    return Todo(**todo)
```

### E. Deleting a Todo

The DELETE endpoint allows users to delete a todo by its `id`.

```python
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos.remove(todo)
    return {"detail": "Todo deleted successfully"}
```

## V. Adding Input Validation and Error Handling

### A. Input Validation with Pydantic

FastAPI automatically validates input data against the Pydantic models we defined. This ensures that the data meets our expected schema before it’s processed.

### B. Custom Error Handling

We can customize error responses by adding an exception handler.

```python
@app.exception_handler(HTTPException)
def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
```

## VI. Testing the API

FastAPI comes with interactive Swagger UI documentation, making it easy to test your API endpoints. Simply run the application and navigate to `/docs` in your browser.

### Testing Example

- **Create a Todo**: Test the POST endpoint by creating a new todo.
- **Retrieve Todos**: Use the GET endpoints to fetch all todos or a specific one by `id`.
- **Update and Delete**: Test the PUT and DELETE endpoints to update or remove a todo.

## VII. Refactoring and Organizing Code

As the application grows, it’s essential to keep the code organized. Here are a few tips:

### A. Moving Models to a Separate File

You can move your Pydantic models to a `models.py` file to keep your main application file clean.

### B. Creating a Router for Todo Endpoints

Consider creating a separate router for todo-related endpoints, especially as your API grows.

## VIII. Next Steps

In the next post, we’ll integrate a real database (like SQLite or PostgreSQL) into our FastAPI application. We’ll also look into user authentication and more advanced features.

### Suggested Improvements:
- Add filtering and pagination to the GET endpoints.
- Implement user authentication to manage personal todos.

## IX. Conclusion

In this tutorial, we built a simple Todo API using FastAPI. We started by designing a data model, implemented CRUD operations, and created endpoints to manage todos. We also touched on input validation, error handling, and testing. With this foundation, you can extend the API further or integrate it with a frontend to create a full-fledged application.
