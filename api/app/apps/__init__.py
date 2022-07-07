import os

from libs.db import Base
from flask import Flask, json, request, jsonify
from flask_jwt_extended import JWTManager #Inisialisasi JWT
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

from .app_doctor.main import blueprint as bp_doctor
from .app_employee.main import blueprint as bp_employee
from .app_patient.main import blueprint as bp_patient
from .app_appointment.main import blueprint as bp_appointment

from settings import settings

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = settings.JWT.SECRET
jwt = JWTManager(app)


# app.register_blueprint(bp, url_prefix='/abc/123')
app.register_blueprint(bp_appointment)

app.register_blueprint(bp_doctor)
app.register_blueprint(bp_employee)
app.register_blueprint(bp_patient)