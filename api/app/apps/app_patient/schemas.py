from typing import Optional, List
from datetime import time, date
from uuid import UUID
# from libs import schemas as app_sch

from pydantic import BaseModel, constr


class PostPatient(BaseModel):
    name        : Optional[str] = None
    no_ktp      : Optional[str] = None
    address     : Optional[str] = None
    birthdate   : Optional[date] = None    
    gender          : Optional[str] = None
    vaccine_type    : Optional[str] = None
    vaccine_count   : Optional[int] = None


class Patient(PostPatient):
    id : Optional[int] 

    class Config:
        orm_mode = True


# class PutPatient(Patient):
#     password    : Optional[str] = None




class PatientsOut(BaseModel):
    message: Optional[str] = "Success"
    data: Optional[List[Patient]]


class PatientOut(BaseModel):
    message: Optional[str] = "Success"
    data: Optional[Patient]
