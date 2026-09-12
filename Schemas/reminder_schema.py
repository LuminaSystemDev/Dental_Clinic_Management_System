from datetime import datetime
from pydantic import BaseModel
from typing import Optional

"""Reminder Schema"""

# Schema for Reminder Base
class ReminderBase(BaseModel):
    appointment_id: int
    type: str
    message: str 
    send_date: datetime
    sent: bool

# Schema for Reminder Create
class ReminderCreate(ReminderBase):
    pass

# Schema for Reminder Update
class ReminderUpdate(BaseModel):
    appointment_id: Optional[int] = None
    type: Optional[str] = None
    message: Optional[str] = None
    send_date: Optional[datetime] = None
    sent: Optional[bool] = None

# Schema for Reminder Response
class ReminderResponse(ReminderBase):
    id: int
    created_at: datetime

# Schema for Reminders List
class RemindersList(BaseModel):
    reminders: list[ReminderResponse]
