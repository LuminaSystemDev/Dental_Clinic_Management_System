from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Text, Date
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Config.db_connection import Base

class Patient(Base):
    __tablename__ = "patients"

    # fields for Patient Model
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(50), nullable=False)
    last_name : Mapped[str] = mapped_column(String(50), nullable=False)
    birth_date : Mapped[datetime] = mapped_column(DateTime, nullable=False)
    gender : Mapped[str] = mapped_column(String(10), nullable=False)
    ci : Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    phone : Mapped[Optional[str]] = mapped_column(String(20))
    email : Mapped[Optional[str]] = mapped_column(String(100), unique=True)
    direction : Mapped[Optional[str]] = mapped_column(String(255))

    medical_history : Mapped[Optional[str]] = mapped_column(Text)
    allergies : Mapped[Optional[str]] = mapped_column(Text)

    created_at : Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Relationship with Appointment Model
    appointments : Mapped[list["Appointment"]] = relationship("Appointment", back_populates="patient")

    # Relationship with MedicalRecord Model
    medical_records : Mapped[list["MedicalRecord"]] = relationship("MedicalRecord", back_populates="patient")

    def __repr__(self):
        return f"<Patient(id={self.id}, name='{self.name}', last_name='{self.last_name}', birth_date={self.birth_date}, gender='{self.gender}', ci='{self.ci}'>"
