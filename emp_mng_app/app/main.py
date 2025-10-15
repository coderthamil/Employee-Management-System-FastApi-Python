# app/main.py
from fastapi import FastAPI
from app.routes.routes import router as api_router
from app.db.session import Base, engine
from app.models.models import User, Employee  # create tables

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management API")

# Include all routes
app.include_router(api_router)
