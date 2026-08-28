from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, DateTime, Text
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Config.db_connection import Base

# Class for Consultation Model
class Consultation(Base):
    __tablename__ = "consultations"

    # fields for Consultation Model
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    appointment_id : Mapped[int] = mapped_column(Integer, ForeignKey("appointments.id"), nullable=False)
    reason : Mapped[str] = mapped_column(String(200), nullable=False)
    diagnosis : Mapped[Optional[str]] = mapped_column(Text)
    treatment : Mapped[Optional[str]] = mapped_column(Text)
    observations : Mapped[Optional[str]] = mapped_column(Text)

    created_at : Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Relationship with Appointment model
    appointment : Mapped["Appointment"] = relationship("Appointment", back_populates="consultation")

    # Relationship with Payment model
    payments : Mapped[list["Payment"]] = relationship("Payment", back_populates="consultation")

    def __repr__(self):
        return f"<Consultation(id={self.id}, appointment_id={self.appointment_id}, reason='{self.reason}', created_at={self.created_at}, updated_at={self.updated_at})>"