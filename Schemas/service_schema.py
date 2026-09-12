from pydantic import BaseModel
from datetime import datetime
from typing import Optional

""" Service Schema """

# Schema for Service Base
class ServiceBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    duration_in_minutes: int
    active: Optional[bool] = True

# Schema for Service Create
class ServiceCreate(ServiceBase):
    pass

# Schema for Service Update
class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    duration_in_minutes: Optional[int] = None
    active: Optional[bool] = True

# Schema for Service Response
class ServiceResponse(ServiceBase):
    id: int
    created_at: datetime
    updated_at: datetime

# Schema for Service List
class ServiceList(BaseModel):
    services: list[ServiceResponse]
