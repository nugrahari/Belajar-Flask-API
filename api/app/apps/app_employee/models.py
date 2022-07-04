from uuid import UUID, uuid4
from typing import List, Dict
from libs import db

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID as sql_UUID
# from sqlalchemy import Column, String, DateTime, text, func, Boolean, Enum, orm, Integer, Text

class EmployeeDB(db.Base):
    __tablename__ = 'employees'
    id = sa.Column(sa.Integer, unique=True, primary_key=True, index=True)
    name        = sa.Column(sa.String(150))
    username    = sa.Column(sa.String(150), unique=True)
    password    = sa.Column(sa.String(255))
    gender      = sa.Column(sa.String(25))
    birthdate   = sa.Column(sa.Date)


    created_at  = sa.Column(sa.DateTime, server_default=sa.func.now())
    updated_at  = sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())

