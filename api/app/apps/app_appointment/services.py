import os
import jwt
import enum
import random
import datetime

from pprint import pprint  # pylint: disable=unused-import
from uuid import UUID, uuid4
from typing import List, Dict

# from sqlalchemy import Column, String, DateTime, text, func, Boolean, Enum, orm, Integer, Text
from sqlalchemy import func
from sqlalchemy.exc import NoResultFound, MultipleResultsFound

from libs import db, schemas
from settings import settings
from flask import Flask, request, jsonify, make_response
from flask import Blueprint, abort

from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from passlib.hash import sha256_crypt

from apps.app_doctor import services as doctor_svc
from apps.app_patient import services as patient_svc
from . import models

class AppointmentServices():
	def __init__(self, db_ ):
		self.db: orm.Session = db_
		self.query: orm.Query = self.db.query(models.AppointmentDB)

	def read_all(self):
		return self.query.all()


	def login(self, login_data):
	
		db_data = self.read_by_username(login_data.username)
		
		if sha256_crypt.verify(login_data.password, db_data.password):
			print("True")
			expires = datetime.timedelta(days=1)
			expires_refresh = datetime.timedelta(days=3)

			access_token = create_access_token({'id': db_data.id, 'username': db_data.username}, 
				fresh=True, expires_delta=expires)
			refresh_token = create_refresh_token(db_data.id, expires_delta=expires_refresh)

			return schemas.ResponseToken(
				message = "Login Success", access_token = access_token, refresh_token = refresh_token)
		else:
			abort(make_response(jsonify(message="Username or Password is invalid"), 400))


	def read_by_username(self, username):
		try:
			return self.query.filter(models.AppointmentDB.username == username).one()
		except NoResultFound as exc:
			abort(make_response(jsonify(message="Username or Password is invalid"), 400))

	def read_by_id(self, id_):
		try:
			return self.query.filter(models.AppointmentDB.id == id_).one()
		except NoResultFound as exc:
			abort(make_response(jsonify(message=F"Appointment with id {id_} is not found"), 404))

	def check_docter_available(self, kwargs, db_doctor):
		first_time = kwargs.datetime-datetime.timedelta(minutes=5)
		last_time = kwargs.datetime+datetime.timedelta(minutes=5)
		db_appointment = self.query.filter(
			models.AppointmentDB.doctor_id == db_doctor.id,
			models.AppointmentDB.status == models.StatusEnum.IN_QUEUE, 
			models.AppointmentDB.datetime.between(first_time, last_time)
			# func.date(models.AppointmentDB.datetime) == dattime.date(),
		).count()
		
		if db_appointment >= 1:
			abort(make_response(jsonify(message=F"Docter {db_doctor.name} sudah ada janji sekitar {kwargs.datetime}"), 400))
		
		if not ((db_doctor.work_start_time < kwargs.datetime.time()) and
					(db_doctor.work_end_time > kwargs.datetime.time())): 
			abort(make_response(jsonify(message=F'Docter {db_doctor.name} tidak ada pada waktu tersebut'), 400))

	def check_docter_available_for_PUT(self, kwargs, db_doctor, id_):
		first_time = kwargs.datetime-datetime.timedelta(minutes=5)
		last_time = kwargs.datetime+datetime.timedelta(minutes=5)
		db_appointment = self.query.filter(
			models.AppointmentDB.id != id_,
			models.AppointmentDB.doctor_id == db_doctor.id,
			models.AppointmentDB.status == models.StatusEnum.IN_QUEUE, 
			models.AppointmentDB.datetime.between(first_time, last_time)
			# func.date(models.AppointmentDB.datetime) == dattime.date(),
		).count()
		
		if db_appointment >= 1:
			abort(make_response(jsonify(message=F"Docter {db_doctor.name} sudah ada janji sekitar {kwargs.datetime}"), 400))
		
		if not ((db_doctor.work_start_time < kwargs.datetime.time()) and
					(db_doctor.work_end_time > kwargs.datetime.time())): 
			abort(make_response(jsonify(message=F'Docter {db_doctor.name} tidak ada pada waktu tersebut'), 400))

	def create(self, kwargs):
		svc_doctor = doctor_svc.DoctorServices(self.db)
		svc_patient = patient_svc.PatientServices(self.db)
		db_doctor = svc_doctor.read_by_id(kwargs.doctor_id)
		db_patient = svc_patient.read_by_id(kwargs.patient_id)

		self.check_docter_available(kwargs, db_doctor)
		
		db_data = models.AppointmentDB(**kwargs.dict())
		self.db.add(db_data)
		self.db.commit()
		return db_data	



	def put_data(self, id_, new_data):
		db_data = self.read_by_id(id_)

		if new_data.doctor_id is not None:
			svc_doctor = doctor_svc.DoctorServices(self.db)
			db_doctor = svc_doctor.read_by_id(new_data.doctor_id)
			db_data.doctor_id = new_data.doctor_id
		
		if new_data.patient_id is not None:
			svc_patient = patient_svc.PatientServices(self.db)
			db_patient = svc_patient.read_by_id(new_data.patient_id)
			db_data.patient_id = new_data.patient_id

		if new_data.datetime is not None:
			svc_doctor = doctor_svc.DoctorServices(self.db)
			db_doctor = svc_doctor.read_by_id(db_data.doctor_id)
			self.check_docter_available_for_PUT(new_data, db_doctor, id_)
			db_data.datetime = new_data.datetime
		
		if new_data.status is not None:
			db_data.status = new_data.status
		
		if new_data.diagnose is not None:
			db_data.diagnose = new_data.diagnose
		
		if new_data.notes is not None:
			db_data.notes = new_data.notes

		self.db.commit()
		return db_data

	def delete(self, id_):
		_ = self.read_by_id(id_)
		self.query.filter(models.AppointmentDB.id == id_).delete()
