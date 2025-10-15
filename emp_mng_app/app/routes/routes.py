# app/routes/routes.py
from fastapi import APIRouter
from app.routes.v1 import auth, employee

router = APIRouter()

# Include the v1 routes
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(employee.router, prefix="/employees", tags=["employees"])
