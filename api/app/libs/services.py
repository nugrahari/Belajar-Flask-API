# import os, random
# from pprint import pprint  # pylint: disable=unused-import
# import enum
# from uuid import UUID, uuid4
# from typing import List, Dict

# from sqlalchemy import Column, String, DateTime, text, func, Boolean, Enum, orm, Integer, Text
# from sqlalchemy.exc import NoResultFound 
# from fastapi import status, HTTPException
from flask_jwt_extended import get_jwt_identity
from libs import db
# from settings import settings

def create_database():
	try:
		return db.Base.metadata.create_all(bind=db.engine)
	except Exception as e:
		print(e)

def my_account():
		# user_data = jwt.decode(token, settings.JWT.SECRET, ["HS256"])
	return get_jwt_identity()