from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

"""Medical Record Schema"""

# Schema for Medical Record
class BaseMedicalRecord(BaseModel):
    patient_id : int
    type_of_record : str
    title : str
    description : Optional[str] = None
    file_path : Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

# Schema for Medical Recors Create
class MedicalRecordCreate(BaseMedicalRecord):
    pass

# Schema for Medical Record Response
class MedicalRecordResponse(BaseMedicalRecord):
    id : int
    created_at : datetime
    updated_at : datetime