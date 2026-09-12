from datetime import datetime
from typing import Optional
from pydantic import BaseModel

""" Roles Schema """

# Schema for Role Base
class BaseRole(BaseModel):
    name: str
    description: Optional[str] = None
    active: Optional[bool] = True

# Schema for Role Create
class RoleCreate(BaseRole):
    pass

# Schema for Role Response
class RoleResponse(BaseRole):
    id: int
    created_at: datetime
    updated_at: datetime

# Schema for Role List
class RoleList(BaseModel):
    roles: list[RoleResponse]
