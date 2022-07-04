import os
import json

from flask import Flask, request, jsonify
from flask import Blueprint, abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import *
from libs import db, services, schemas

from . import services as svc, schemas as sch

# from apps import jwt



blueprint = Blueprint('patient', __name__)

# @blueprint.route('/login', methods=['POST'])
# def login_patients():

# 	login_form = schemas.Login(**request.form)
# 	with db.session() as db_:
# 		patient_svc = svc.PatientServices(db_)
# 		response = patient_svc.login(login_form) 		
		
# 	return response.dict(), 200

# @blueprint.route('/employee/my-account', methods=['GET'])
# @jwt_required( )
# def account_patients():	
# 	employee = services.my_account()
# 	return employee, 200

@blueprint.route('/patients', methods=['GET'])
@jwt_required( )
def get_patients():

	with db.session() as db_:
		patient_svc = svc.PatientServices(db_)
		patient_db = patient_svc.read_all() 		
		patient_schema = sch.PatientsOut(data = patient_db)


	return json.dumps(patient_schema.dict(), default=str), 200

@blueprint.route('/patients', methods=['POST'])
@jwt_required( )
def post_patient():
	new_patient = sch.PostPatient(**request.form)
	
	with db.session() as db_:
		patient_svc = svc.PatientServices(db_)
		patient_db = patient_svc.create(new_patient) 
		patient_schema = sch.PatientOut(data=patient_db)

	return json.dumps(patient_schema.dict(), default=str), 201
	

@blueprint.route('/patients/<id_patient>', methods=['GET'])
@jwt_required( )
def get_patient(id_patient:int):

	with db.session() as db_:
		patient_svc = svc.PatientServices(db_)
		patient_db = patient_svc.read_by_id(id_patient) 		
		patient_schema = sch.PatientOut(data = patient_db)

	return json.dumps(patient_schema.dict(), default=str), 200

@blueprint.route('/patients/<id_patient>', methods=['PUT'])
@jwt_required( )
def put_patient(id_patient:int):
	new_data = sch.PostPatient(**request.form)

	with db.session() as db_:
		patient_svc = svc.PatientServices(db_)
		patient_db = patient_svc.put_data(id_patient, new_data) 		
		patient_schema = sch.PatientOut(data = patient_db)

	return json.dumps(patient_schema.dict(), default=str), 200

@blueprint.route('/patients/<id_patient>', methods=['DELETE'])
@jwt_required( )
def delete_patient(id_patient:int):

	with db.session() as db_:
		patient_svc = svc.PatientServices(db_)
		patient_db = patient_svc.delete(id_patient) 		

	return '', 204


