import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import events
from utils.db import engine  # Import the engine from db.py

# Initialize the database
try:
    with engine.connect() as connection:
        print("Database connection successful!")
except Exception as e:
    print(f"Failed to connect to the database: {e}")

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify your Grafana domain)
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Universidad EIA"}

# Include the events router
app.include_router(events.router)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("app_port", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)