"""RESTAPI FOR THE MANAGEMENT OF DENTAL CONSULTATIONS AND SERVICES"""

# Imports
from fastapi import FastAPI
from Routers.User import user_router
from Routers.Auth import auth_user_router

# API
app = FastAPI(
    title="Dental Clinic Management System",
    description="RESTAPI FOR THE MANAGEMENT OF DENTAL CONSULTATIONS AND SERVICES",
    )

# Include Routers
app.include_router(user_router)
app.include_router(auth_user_router)

# Principal Route
@app.get("/")
def get_root():
    return {"NameProyect": "Dental Clinic Management System",
            "PythonVersion": "3.14",
            "Documentation": "http://127.0.0.1:8000/docs"}