from datetime import datetime
from pydantic import BaseModel, ConfigDict

"""Payment Schema"""

# Schema for Payment Base
class PaymentBase(BaseModel):
    consultation_id : int
    total_amount : float
    amount_paid : float
    payment_type : str
    payment_method : str
    payment_date : datetime
    payment_receipt : str

    model_config = ConfigDict(from_attributes=True)

# Schema for Payment Create
class PaymentCreate(PaymentBase):
    pass

# Schema for Payment Response 
class PaymentResponse(PaymentBase):
    id : int
    created_at : datetime
    updated_at : datetime


