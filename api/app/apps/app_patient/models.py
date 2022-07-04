from uuid import UUID, uuid4
from typing import List, Dict
from libs import db

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID as sql_UUID
# from sqlalchemy import Column, String, DateTime, text, func, Boolean, Enum, orm, Integer, Text

class PatientDB(db.Base):
	__tablename__ = 'patients'
	id = sa.Column(sa.Integer, unique=True, primary_key=True, index=True)
	name 		= sa.Column(sa.String(150))
	no_ktp      = sa.Column(sa.String(150), unique=True)
	address 	= sa.Column(sa.Text)
	gender 		= sa.Column(sa.String(25))
	birthdate 	= sa.Column(sa.Date)
	vaccine_type    = sa.Column(sa.String(150))
	vaccine_count   = sa.Column(sa.Integer)


	created_at 	= sa.Column(sa.DateTime, server_default=sa.func.now())
	updated_at 	= sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())

