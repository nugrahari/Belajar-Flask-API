from typing import Optional, List
from datetime import date
from uuid import UUID
# from libs import schemas as app_sch

from pydantic import BaseModel, constr


class Employee(BaseModel):
    id          : Optional[int] 
    name        : Optional[str] = None
    username    : Optional[str] = None
    gender      : Optional[str] = None
    birthdate   : Optional[date] = None

    class Config:
        orm_mode = True


class PutEmployee(Employee):
    password    : Optional[str] = None


class PostEmployee(Employee):
    password    : str


class EmployeesOut(BaseModel):
    message: Optional[str] = "Success"
    data: Optional[List[Employee]]


class EmployeeOut(BaseModel):
    message: Optional[str] = "Success"
    data: Optional[Employee]
