"""RESTAPI FOR THE MANAGEMENT OF DENTAL CONSULTATIONS AND SERVICES"""

# Imports
from fastapi import FastAPI

# API
app = FastAPI()

# Principal Route
@app.get("/")
def get_root():
    return {"NameProyect": "Dental Clinic Management System",
            "PythonVersion": "3.14",
            "Documentation": "http://127.0.0.1:8000/docs"}