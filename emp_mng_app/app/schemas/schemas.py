from pydantic import BaseModel, EmailStr, constr
from datetime import datetime

# USER SCHEMAS
class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=6, max_length=72)

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True  # For Pydantic v2

# EMPLOYEE SCHEMAS
class EmployeeBase(BaseModel):
    first_name: constr(min_length=2, max_length=50)
    last_name: constr(min_length=2, max_length=50)
    position: constr(min_length=2, max_length=50)
    salary: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
