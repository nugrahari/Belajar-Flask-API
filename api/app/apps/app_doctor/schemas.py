from typing import Optional, List
from datetime import time, date
from uuid import UUID
# from libs import schemas as app_sch

from pydantic import BaseModel, constr


class Doctor(BaseModel):
    id          : Optional[int] 
    name        : Optional[str] = None
    username    : Optional[str] = None
    gender      : Optional[str] = None
    birthdate   : Optional[date] = None
    work_start_time : Optional[time] = None
    work_end_time : Optional[time] = None

    class Config:
        orm_mode = True


class PutDoctor(Doctor):
    password    : Optional[str] = None


class PostDoctor(Doctor):
    password    : str


class DoctorsOut(BaseModel):
    message: Optional[str] = "Success"
    data: Optional[List[Doctor]]


class DoctorOut(BaseModel):
    message: Optional[str] = "Success"
    data: Optional[Doctor]
