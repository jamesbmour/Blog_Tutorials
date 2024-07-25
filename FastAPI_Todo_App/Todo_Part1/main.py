from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Todo App!"}

@app.get("/current-time")
async def get_current_time():
    current_time = datetime.now()
    return {
        "current_date": current_time.strftime("%Y-%m-%d"),
        "current_time": current_time.strftime("%H:%M:%S"),
        "timezone": current_time.astimezone().tzname()
    }
