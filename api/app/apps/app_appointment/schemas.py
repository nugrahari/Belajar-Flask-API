from typing import Optional, List
from datetime import time, datetime, date
from uuid import UUID
# from libs import schemas as app_sch

from pydantic import BaseModel, constr

from . import models


class PostAppointment(BaseModel):
    patient_id  : int
    doctor_id   : int
    datetime    : datetime
    status      : Optional[models.StatusEnum] = None 
    diagnose    : Optional[str] = None
    notes       : Optional[str] = None

    # class Config:
    #     use_enum_values = True

class PutAppointment(BaseModel):
    patient_id  : Optional[int] = None
    doctor_id   : Optional[int] = None
    datetime    : Optional[datetime] #= None
    status      : Optional[models.StatusEnum] = None
    diagnose    : Optional[str] = None
    notes       : Optional[str] = None

class Appointment(PostAppointment):
    id : Optional[int] 

    class Config:
        orm_mode = True


class AppointmentsOut(BaseModel):
    message: Optional[str] = "Success"
    data: Optional[List[Appointment]]


class AppointmentOut(BaseModel):
    message: Optional[str] = "Success"
    data: Optional[Appointment]
