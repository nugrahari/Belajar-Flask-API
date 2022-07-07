from typing import Optional, List
from datetime import date
from uuid import UUID
# from libs import schemas as app_sch

from pydantic import BaseModel, constr

class PostEmployee(BaseModel):
    name        : Optional[str] = None
    username    : Optional[str] = None
    gender      : Optional[str] = None
    birthdate   : Optional[date] = None
    password    : str



class PutEmployee(BaseModel):
    name        : Optional[str] = None
    username    : Optional[str] = None
    gender      : Optional[str] = None
    birthdate   : Optional[date] = None
    
    password    : Optional[str] = None


class Employee(PutEmployee):
    id          : Optional[int] 

    class Config:
        orm_mode = True


class EmployeesOut(BaseModel):
    message: Optional[str] = "Success"
    data: Optional[List[Employee]]


class EmployeeOut(BaseModel):
    message: Optional[str] = "Success"
    data: Optional[Employee]
