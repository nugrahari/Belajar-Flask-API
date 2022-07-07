import os
import json

from flask import Flask, request, jsonify
from flask import Blueprint, abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import *
from libs import db, services, schemas

from . import services as svc, schemas as sch

# from apps import jwt



blueprint = Blueprint('doctor', __name__)

# @blueprint.route('/login', methods=['POST'])
# def login_doctors():

# 	login_form = schemas.Login(**request.form)
# 	with db.session() as db_:
# 		doctor_svc = svc.DoctorServices(db_)
# 		response = doctor_svc.login(login_form) 		
		
# 	return response.dict(), 200

# @blueprint.route('/employee/my-account', methods=['GET'])
# @jwt_required( )
# def account_doctors():	
# 	employee = services.my_account()
# 	return employee, 200

@blueprint.route('/doctors', methods=['GET'])
@jwt_required( )
def get_doctors():

	with db.session() as db_:
		doctor_svc = svc.DoctorServices(db_)
		doctor_db = doctor_svc.read_all() 		
		doctor_schema = sch.DoctorsOut(data = doctor_db)


	return json.dumps(doctor_schema.dict(), default=str), 200

@blueprint.route('/doctors', methods=['POST'])
@jwt_required( )
def post_doctor():
	new_doctor = sch.PostDoctor(**request.form)
	
	with db.session() as db_:
		doctor_svc = svc.DoctorServices(db_)
		doctor_db = doctor_svc.create(new_doctor) 
		doctor_schema = sch.DoctorOut(data=doctor_db)

	return json.dumps(doctor_schema.dict(), default=str), 201
	

@blueprint.route('/doctors/<id_doctor>', methods=['GET'])
@jwt_required( )
def get_doctor(id_doctor:int):

	with db.session() as db_:
		doctor_svc = svc.DoctorServices(db_)
		doctor_db = doctor_svc.read_by_id(id_doctor) 		
		doctor_schema = sch.DoctorOut(data = doctor_db)

	return json.dumps(doctor_schema.dict(), default=str), 200

@blueprint.route('/doctors/<id_doctor>', methods=['PUT'])
@jwt_required( )
def put_doctor(id_doctor:int):
	new_data = sch.PutDoctor(**request.form)

	with db.session() as db_:
		doctor_svc = svc.DoctorServices(db_)
		doctor_db = doctor_svc.put_data(id_doctor, new_data) 		
		doctor_schema = sch.DoctorOut(data = doctor_db)

	return json.dumps(doctor_schema.dict(), default=str), 200

@blueprint.route('/doctors/<id_doctor>', methods=['DELETE'])
@jwt_required( )
def delete_doctor(id_doctor:int):

	with db.session() as db_:
		doctor_svc = svc.DoctorServices(db_)
		doctor_db = doctor_svc.delete(id_doctor) 		

	return '', 204


