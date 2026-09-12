from typing import Optional
from datetime import datetime
from pydantic import BaseModel

"""Appointment Schema"""

# Schema for Appointment Base
class AppointmentBase(BaseModel):
    patient_id: int
    dentist_id: int
    service_id: int
    init_date_time: datetime
    end_date_time: datetime
    shift: str
    status: str
    notes: Optional[str] = None

# Schema for Appointment Create
class AppointmentCreate(AppointmentBase):
    pass

# Schema for Appointment Update
class AppointmentUpdate(AppointmentBase):
    patient_id: Optional[int] = None
    dentist_id: Optional[int] = None
    service_id: Optional[int] = None
    init_date_time: Optional[datetime] = None
    end_date_time: Optional[datetime] = None
    shift: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None

# Schema for Appointment Response
class AppointmentResponse(AppointmentBase):
    id: int
    created_at: datetime
    updated_at: datetime

# Schema for Appointments List
class AppointmentList(BaseModel):
    appointments: list[AppointmentResponse]
