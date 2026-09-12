from typing import Optional
from datetime import datetime
from pydantic import BaseModel

"""Consultation Schema"""

# Schema for consultation base
class ConsultationBase(BaseModel):
    appointment_id : int
    reason : str
    diagnosis : Optional[str] = None
    treatment : Optional[str] = None
    observations : Optional[str] = None

# Schema for consultation Create
class ConsultationCreate(ConsultationBase):
    pass

# Schema for consultation Response
class ConsultationResponse(ConsultationBase):
    id : int
    created_at : datetime
    updated_at : datetime

# Schema for Consultations List
class ConsultationsList(BaseModel):
    consultations : list[ConsultationResponse]