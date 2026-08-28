from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, DateTime, Text
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Config.db_connection import Base

# Class for Appointment Model
class Appointment(Base):
    __tablename__ = "appointments"

    # fields for Appointment Model
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    patient_id : Mapped[int] = mapped_column(Integer, ForeignKey("patients.id"), nullable=False)
    dentist_id : Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    service_id : Mapped[int] = mapped_column(Integer, ForeignKey("services.id"), nullable=False)

    init_date_time : Mapped[datetime] = mapped_column(DateTime, nullable=False) 
    end_date_time : Mapped[datetime] = mapped_column(DateTime, nullable=False)

    shift : Mapped[str] = mapped_column(String(50), nullable=False)
    status : Mapped[str] = mapped_column(String(50), nullable=False)

    notes : Mapped[Optional[str]] = mapped_column(Text)

    created_at : Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships with other models
    patient : Mapped["Patient"] = relationship("Patient", back_populates="appointments")
    dentist : Mapped["User"] = relationship("User", back_populates="appointments")
    service : Mapped["Service"] = relationship("Service", back_populates="appointments")

    # Relationship with Consultation model
    consultation : Mapped[Optional["Consultation"]] = relationship("Consultation", back_populates="appointment", uselist=False)

    # Relationship with Reminder Model
    reminders: Mapped[list["Reminder"]] = relationship("Reminder", back_populates="appointment")

    def __repr__(self):
        return f"<Appointment(id={self.id}, patient_id={self.patient_id}, dentist_id={self.dentist_id}, service_id={self.service_id}, init_date_time={self.init_date_time}, end_date_time={self.end_date_time}, shift='{self.shift}', status='{self.status}', created_at={self.created_at}, updated_at={self.updated_at})>"