from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, String, Boolean, DateTime, Numeric 
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Config.db_connection import Base

# Class for Service Model
class Service(Base):
    __tablename__ = "services"

    # fields for Service Model
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description : Mapped[Optional[str]] = mapped_column(String(255))
    price : Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    duration_in_minutes : Mapped[int] = mapped_column(Integer, nullable=False) 
    active : Mapped[bool] = mapped_column(Boolean, default=True)
    created_at : Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Relationship with Appointment Model
    appointments : Mapped[list["Appointment"]] = relationship("Appointment", back_populates="service")
    
    def __repr__(self):
        return f"<Service(id={self.id}, name='{self.name}', description='{self.description}', price={self.price}, duration_in_minutes={self.duration_in_minutes}, active={self.active}, created_at={self.created_at}, updated_at={self.updated_at})>"
