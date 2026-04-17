from fastapi import FastAPI
from database import Base, engine
from routers import employee

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(employee.router)

@app.get("/")
def home():
    return {"message": "FastAPI Modular App Running"}
