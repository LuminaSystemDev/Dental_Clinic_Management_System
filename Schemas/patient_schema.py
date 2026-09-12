from pydantic import BaseModel
from typing import Optional
from datetime import datetime

""" Patient Schema """

# Schema for Patient Base
class BasePatient(BaseModel):
    name : str
    last_name : str
    birth_date : datetime
    gender : str
    ci : str
    phone : Optional[str] = None
    email : Optional[str] = None
    direction : Optional[str] = None
    medical_history : Optional[str] = None
    allergies : Optional[str] = None

# Schema for Patient Create
class PatientCreate(BasePatient):
    pass

# Schema for Patient Update
class PatientUpdate(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[datetime] = None
    gender: Optional[str] = None
    ci: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    direction: Optional[str] = None
    medical_history: Optional[str] = None
    allergies: Optional[str] = None

# Schema for Patient Response
class PatientResponse(BasePatient):
    id : int
    created_at : datetime
    updated_at : datetime

# Schema for Patient List
class PatientList(BaseModel):
    patients : list[PatientResponse]

