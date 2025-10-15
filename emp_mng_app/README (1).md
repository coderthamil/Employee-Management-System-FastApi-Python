
# Employee Management API with JWT Authentication

A brief description of what this project does and who it's for

Employee Management API with JWT Authentication

Project Overview:
This project is a RESTful API built using FastAPI for managing employees in an organization. It supports CRUD operations for employees and user accounts, with secure authentication using JWT (JSON Web Tokens) and HTTP Bearer tokens.

Key Features:

User Management:

Register new users with hashed passwords.

Login with JWT access token generation.

Retrieve current user details via token.

Employee Management:

Create, read, update, and delete employee records.

Each employee record stores first name, last name, position, salary, and creation timestamp.

Authentication & Authorization:

Uses JWT tokens for secure access to protected endpoints.

HTTP Bearer authentication for all sensitive routes.

Token validation ensures that only authorized users can perform employee CRUD operations.

Database:

Uses SQLAlchemy ORM for interaction with a PostgreSQL or SQLite database.

Models are defined for User and Employee.
========================================================================================
Folder Structure:
=========

app/
├─ core/
│  └─ security.py           # JWT, password hashing, authentication helpers
├─ db/
│  ├─ models/
│  │  └─ models.py          # SQLAlchemy ORM models
│  └─ schemas/
│     └─ schemas.py         # Pydantic schemas for request/response validation
├─ routes/
│  └─ v1/
│     ├─ auth.py            # User registration/login routes
│     └─ employee.py        # Employee CRUD routes
│  └─ routes.py             # Combines all v1 routes for main app
├─ main.py                  # FastAPI app instance and router inclusion
├─ .env                     # Environment variables (SECRET_KEY, DB_URL, etc.)
└─ db/
   └─ session.py            # Database session setup
===========================================================================================
## Installation


Steps to Run:
1️⃣ Clone or Navigate to Your Project:
bash:
cd path/to/emp_mng_app

2️⃣ Create Virtual Environment (Optional but Recommended)
bash:
python -m venv .venv


Activate the virtual environment:

Windows:

.venv\Scripts\activate


Linux/Mac:

source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt, you can install manually:

pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv passlib[bcrypt] python-jose pydantic

4️⃣ Setup Environment Variables

Create a .env file in the root directory with contents like:

SECRET_KEY=your_super_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=postgresql://username:password@localhost:5432/your_db_name


Make sure to replace the database URL and credentials.
## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform


## Feedback

If you have any feedback, please reach out to us at senthamiln4@gmail.com


## 🛠 Skills

Python , FastAPI, Database-PostgreSQL , API concepts