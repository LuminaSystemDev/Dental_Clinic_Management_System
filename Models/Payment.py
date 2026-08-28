from datetime import datetime
from sqlalchemy import func
from sqlalchemy import Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from Config.db_connection import Base

# Class for Payment Model
class Payment(Base):
    __tablename__ = "payments"

    # Fields for Payment Model
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    consultation_id : Mapped[int] = mapped_column(Integer, ForeignKey("consultations.id"), nullable=False)
    total_amount : Mapped[float] = mapped_column(Numeric(10, 2), nullable=False) 
    amount_paid : Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    payment_type : Mapped[str] = mapped_column(String(50), nullable=False)
    payment_method : Mapped[str] = mapped_column(String(50), nullable=False)
    payment_date : Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    payment_receipt : Mapped[str] = mapped_column(String(100), nullable=False)

    created_at : Mapped[datetime] = mapped_column(DateTime, default=func.now()) 
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Relationship with Consultation Model
    consultation : Mapped["Consultation"] = relationship("Consultation", back_populates="payments")

    def __repr__(self):
        return f"<Payment(id={self.id}, consultation_id={self.consultation_id}, total_amount={self.total_amount}, amount_paid={self.amount_paid}, payment_type='{self.payment_type}', payment_method='{self.payment_method}', payment_date='{self.payment_date}', created_at={self.created_at}, updated_at={self.updated_at})>"