from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from Config.db_connection import Base

# Class for User Model 
class User(Base):
    __tablename__ = "users"

    # fields for User Model
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(50), nullable=False) 
    last_name : Mapped[str] = mapped_column(String(50), nullable=False)
    email : Mapped[Optional[str]] = mapped_column(String(100), unique=True)
    phone_number : Mapped[Optional[str]] = mapped_column(String(20), unique=True)
    hashed_password : Mapped[str] = mapped_column(String(255), nullable=False)
    active : Mapped[bool] = mapped_column(Boolean, default=True)
    created_at : Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Foreign key to Role model
    role_id : Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"), nullable=False)

    # Relationship with Role model
    role: Mapped["Role"] = relationship("Role", back_populates="users")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', last_name='{self.last_name}', email='{self.email}', phone_number='{self.phone_number}', active={self.active}, created_at={self.created_at}, updated_at={self.updated_at})>"