import os

from flask import Flask, request, jsonify
from flask import Blueprint, abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import *
from libs import db, services, schemas

from . import services as svc, schemas as sch

# from apps import jwt



blueprint = Blueprint('employee', __name__)

@blueprint.route('/login', methods=['POST'])
def login_employees():

	login_form = schemas.Login(**request.form)
	with db.session() as db_:
		employee_svc = svc.EmployeeServices(db_)
		response = employee_svc.login(login_form) 		
		
	return response.dict(), 200

@blueprint.route('/employee/my-account', methods=['GET'])
@jwt_required( )
def account_employees():	
	employee = services.my_account()
	return employee, 200

@blueprint.route('/employees', methods=['GET'])
@jwt_required( )
def get_employees():

	with db.session() as db_:
		employee_svc = svc.EmployeeServices(db_)
		employee_db = employee_svc.read_all() 		
		employee_schema = sch.EmployeesOut(data = employee_db)

	return employee_schema.dict(), 200

@blueprint.route('/employees', methods=['POST'])
@jwt_required( )
def post_employee():
	new_employee = sch.PostEmployee(**request.form)
	
	with db.session() as db_:
		employee_svc = svc.EmployeeServices(db_)
		employee_db = employee_svc.create(new_employee) 
		employee_schema = sch.EmployeeOut(data=employee_db)

	return employee_schema.dict(), 201

@blueprint.route('/employees/<id_employee>', methods=['GET'])
@jwt_required( )
def get_employee(id_employee:int):

	with db.session() as db_:
		employee_svc = svc.EmployeeServices(db_)
		employee_db = employee_svc.read_by_id(id_employee) 		
		employee_schema = sch.EmployeeOut(data = employee_db)

	return employee_schema.dict(), 200

@blueprint.route('/employees/<id_employee>', methods=['PUT'])
@jwt_required( )
def put_employee(id_employee:int):
	new_data = sch.PutEmployee(**request.form)

	with db.session() as db_:
		employee_svc = svc.EmployeeServices(db_)
		employee_db = employee_svc.put_data(id_employee, new_data) 		
		employee_schema = sch.EmployeeOut(data = employee_db)

	return employee_schema.dict(), 200

@blueprint.route('/employees/<id_employee>', methods=['DELETE'])
@jwt_required( )
def delete_employee(id_employee:int):

	with db.session() as db_:
		employee_svc = svc.EmployeeServices(db_)
		employee_db = employee_svc.delete(id_employee) 		

	return '', 204


