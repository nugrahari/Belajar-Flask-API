import os
import json

from flask import Flask, request, jsonify
from flask import Blueprint, abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import *
from libs import db, services, schemas

from . import services as svc, schemas as sch

# from apps import jwt



blueprint = Blueprint('appointment', __name__)

# @blueprint.route('/login', methods=['POST'])
# def login_appointments():

# 	login_form = schemas.Login(**request.form)
# 	with db.session() as db_:
# 		appointment_svc = svc.AppointmentServices(db_)
# 		response = appointment_svc.login(login_form) 		
		
# 	return response.dict(), 200

# @blueprint.route('/employee/my-account', methods=['GET'])
# @jwt_required( )
# def account_appointments():	
# 	employee = services.my_account()
# 	return employee, 200

@blueprint.route('/appointments', methods=['GET'])
@jwt_required( )
def get_appointments():

	with db.session() as db_:
		appointment_svc = svc.AppointmentServices(db_)
		appointment_db = appointment_svc.read_all() 		
		appointment_schema = sch.AppointmentsOut(data = appointment_db).json()


	return appointment_schema, 200

@blueprint.route('/appointments', methods=['POST'])
@jwt_required( )
def post_appointment():
	new_appointment = sch.PostAppointment(**request.form)
	
	with db.session() as db_:
		appointment_svc = svc.AppointmentServices(db_)
		appointment_db = appointment_svc.create(new_appointment) 
		appointment_schema = sch.AppointmentOut(data=appointment_db).json()

	return appointment_schema, 201
	

@blueprint.route('/appointments/<id_appointment>', methods=['GET'])
@jwt_required( )
def get_appointment(id_appointment:int):

	with db.session() as db_:
		appointment_svc = svc.AppointmentServices(db_)
		appointment_db = appointment_svc.read_by_id(id_appointment) 		
		appointment_schema = sch.AppointmentOut(data = appointment_db).json()
	return appointment_schema, 200
	# return appointment_schema.dict(), 200

@blueprint.route('/appointments/<id_appointment>', methods=['PUT'])
@jwt_required( )
def put_appointment(id_appointment:int):
	new_data = sch.PutAppointment(**request.form)

	with db.session() as db_:
		appointment_svc = svc.AppointmentServices(db_)
		appointment_db = appointment_svc.put_data(id_appointment, new_data) 		
		appointment_schema = sch.AppointmentOut(data = appointment_db).json()

	return appointment_schema, 200

@blueprint.route('/appointments/<id_appointment>', methods=['DELETE'])
@jwt_required( )
def delete_appointment(id_appointment:int):

	with db.session() as db_:
		appointment_svc = svc.AppointmentServices(db_)
		appointment_db = appointment_svc.delete(id_appointment) 		

	return '', 204


