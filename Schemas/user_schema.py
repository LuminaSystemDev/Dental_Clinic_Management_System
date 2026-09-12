from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

""" User Schema """

# Schema for User Base
class BaseUser(BaseModel):
    name: str
    last_name: str
    email: Optional[str] = None
    phone_number: Optional[str] = None
    active: Optional[bool] = True

    role_id: int

# Schema for User Create
class UserCreate(BaseUser):
    hashed_password: str

# Schema for User Update
class UserUpdate(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    active: Optional[bool] = True
    role_id: Optional[int] = None

    hashed_password: Optional[str] = None

# Schema for User Response
class UserResponse(BaseUser):
    id: int
    created_at: datetime
    updated_at: datetime

# Schema for User List
class UserList(BaseModel):
    users: list[UserResponse]

# Schema for User Login
class UserLogin(BaseModel):
    email: str
    password: str
