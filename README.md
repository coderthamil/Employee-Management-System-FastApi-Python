app/
├─ core/security.py
├─ db/
│  ├─ models/models.py
│  ├─ schemas/schemas.py
│  └─ session.py
├─ routes/
│  ├─ v1/auth.py
│  ├─ v1/employee.py
│  └─ routes.py       <-- imports v1 routes and combines them
├─ main.py
└─ .env
