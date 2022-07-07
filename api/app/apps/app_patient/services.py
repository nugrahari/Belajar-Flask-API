import os
import jwt
import enum
import random
import datetime

from pprint import pprint  # pylint: disable=unused-import
from uuid import UUID, uuid4
from typing import List, Dict

# from sqlalchemy import Column, String, DateTime, text, func, Boolean, Enum, orm, Integer, Text
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

from . import models

class PatientServices():
	def __init__(self, db_ ):
		self.db: orm.Session = db_
		self.query: orm.Query = self.db.query(models.PatientDB)

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
			return self.query.filter(models.PatientDB.username == username).one()
		except NoResultFound as exc:
			abort(make_response(jsonify(message="Username or Password is invalid"), 400))

	def read_by_id(self, id_):
		try:
			return self.query.filter(models.PatientDB.id == id_).one()
		except NoResultFound as exc:
			abort(make_response(jsonify(message=F"Patient with id {id_} is not found"), 404))

	def create(self, kwargs):
		# kwargs.password = sha256_crypt.encrypt(kwargs.password)
		try:
			db_data = models.PatientDB(**kwargs.dict())
			self.db.add(db_data)
			self.db.commit()
			return db_data
			
		except Exception as e:	
			abort(make_response(jsonify(message=F'{e}'), 400))

	def put_data(self, id_, new_data):
		db_data = self.read_by_id(id_)

		if new_data.name is not None:
			db_data.name = new_data.name
		if new_data.address is not None:
			db_data.address = new_data.address
		if new_data.gender is not None:
			db_data.gender = new_data.gender
		if new_data.birthdate is not None:
			db_data.birthdate = new_data.birthdate
		if new_data.no_ktp is not None:
			db_data.no_ktp = new_data.no_ktp
		if new_data.vaccine_type is not None:
			db_data.vaccine_type = new_data.vaccine_type
		if new_data.vaccine_count is not None:
			db_data.vaccine_count = new_data.vaccine_count

		self.db.commit()
		return db_data

	def delete(self, id_):
		_ = self.read_by_id(id_)
		self.query.filter(models.PatientDB.id == id_).delete()
