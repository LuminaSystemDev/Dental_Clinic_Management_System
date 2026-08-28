from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Config.db_connection import Base

# Class for MedicalRecord Model
class MedicalRecord(Base):
    __tablename__ = "medical_records"

    # Fields for MedicalRecord Model
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey("patients.id"), nullable=False)
    type_of_record: Mapped[str] = mapped_column(String(50), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    file_path: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Relationship with Patient model
    patient: Mapped["Patient"] = relationship("Patient", back_populates="medical_records")

    def __repr__(self):
        return f"<MedicalRecord(id={self.id}, patient_id={self.patient_id}, type_of_record={self.type_of_record}, title={self.title}, description='{self.description}')>"