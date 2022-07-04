from uuid import UUID, uuid4
from typing import List, Dict
from libs import db

import enum
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID as sql_UUID
# from sqlalchemy import Column, String, DateTime, text, func, Boolean, Enum, orm, Integer, Text

class StatusEnum(enum.Enum):
	IN_QUEUE: str = 'IN_QUEUE'  # pylint: disable=invalid-name
	CANCELLED: str = 'CANCELLED'  # pylint: disable=invalid-name
	DONE: str = 'DONE'  # pylint: disable=invalid-name


class AppointmentDB(db.Base):
	__tablename__ = 'appointments'
	id = sa.Column(sa.Integer, unique=True, primary_key=True, index=True)
	patient_id 	= sa.Column(sa.Integer)
	doctor_id 	= sa.Column(sa.Integer)
	datetime 	= sa.Column(sa.DateTime)
	status = sa.Column(sa.Enum(StatusEnum), server_default="IN_QUEUE")
	diagnose = sa.Column(sa.Text)
	notes = sa.Column(sa.Text)


	created_at 	= sa.Column(sa.DateTime, server_default=sa.func.now())
	updated_at 	= sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())

	