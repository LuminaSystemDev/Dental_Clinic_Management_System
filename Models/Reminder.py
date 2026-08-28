from sqlalchemy import func
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Config.db_connection import Base

# Class for Reminder Model
class Reminder(Base):
    __tablename__ = "reminders"

    # fields for Reminder Model
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    appointment_id : Mapped[int] = mapped_column(Integer, ForeignKey("appointments.id"), nullable=False)
    type : Mapped[str] = mapped_column(String(50), nullable=False)
    message : Mapped[str] = mapped_column(String(500), nullable=False)
    send_date : Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    sent : Mapped[bool] = mapped_column(Boolean, default=False)

    created_at : Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    # Relationship with Appointment Model
    appointment : Mapped["Appointment"] = relationship("Appointment", back_populates="reminders")

    def __repr__(self):
        return f"<Reminder(id={self.id}, appointment_id={self.appointment_id}, type='{self.type}', message='{self.message}', send_date={self.send_date}, sent={self.sent}, created_at={self.created_at})>"