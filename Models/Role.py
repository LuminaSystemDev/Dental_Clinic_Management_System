from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, String, Boolean, DateTime, Enum as SQLEnum
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column 
from sqlalchemy.orm import relationship

from Config.db_connection import Base

# Class for Role Model
class Role(Base):
    __tablename__ = "roles"

    # fields for Role Model
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description : Mapped[Optional[str]] = mapped_column(String(200))
    active : Mapped[bool] = mapped_column(Boolean, default=True)
    created_at : Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Inverse relationship with User model
    users: Mapped[list["User"]] = relationship("User", back_populates="role")

    def __repr__(self):
        return f"<Role(id={self.id}, name='{self.name}', description='{self.description}', active={self.active}, created_at={self.created_at}, updated_at={self.updated_at})>"