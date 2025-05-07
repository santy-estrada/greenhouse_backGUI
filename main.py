from fastapi import FastAPI
from routers import events
from utils.db import engine  # Import the engine from db.py

# Initialize the database
try:
    with engine.connect() as connection:
        print("Database connection successful!")
except Exception as e:
    print(f"Failed to connect to the database: {e}")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Universidad EIA"}

# Include the events router
app.include_router(events.router)