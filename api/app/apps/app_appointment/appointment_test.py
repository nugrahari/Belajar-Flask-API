import os
import requests

url_base = 'http://127.0.0.1:5000/'
token = None
id_appointment = None
id_appointment_2 = None
id_patient = None
id_doctor = None
body = {}


def item_response(response):
	assert 'message' in response
	assert 'data' in response

def test_post_patient(admin1_token):
	global token, id_patient, body
	token = admin1_token
	url_post =  F'{url_base}patients'
	headers = {"Authorization": F"Bearer {token}"}
	body = {
		'name'		: "Hata Rajasa",
		'no_ktp' 	: "6745673456345634",
		'address' 	: "Banjar Sari",
		'gender'	: "laki-laki",
		'birthdate'	: "1988-02-25",
		'vaccine_type': 'Astro',
		'vaccine_count': 2
	}
	reqs = requests.post(url_post, headers=headers, data=body)

	assert reqs.status_code == 201
	response = reqs.json()

	item_response(response)

	data = response.get('data')
	# print(type(data))
	id_patient = data['id']


def test_post_docter():
	global token, id_doctor, body
	url_post =  F'{url_base}doctors'
	headers = {"Authorization": F"Bearer {token}"}
	body = {
		'username' 	: "mustofa",
		'name'		: "Hata Rajasa",
		'password' 	: "maryati",
		'gender'	: "laki-laki",
		'birthdate'	: "1988-02-25",
		'work_start_time': '07:55:33',
		'work_end_time': '23:00:59'
	}
	reqs = requests.post(url_post, headers=headers, data=body)

	assert reqs.status_code == 201
	response = reqs.json()

	item_response(response)

	data = response.get('data')
	# print(type(data))
	id_doctor = data['id']


def test_post():
	global token, id_appointment, body, id_appointment_2
	url_post =  F'{url_base}appointments'
	headers = {"Authorization": F"Bearer {token}"}
	body = {
		'doctor_id'		: id_doctor,
		'patient_id' 	: id_patient,
		'datetime' 	: "2022-12-12T23:20:00"
	}
	reqs = requests.post(url_post, headers=headers, data=body)

	assert reqs.status_code == 400

	body['datetime'] = "2022-12-12T11:20:00"
	reqs = requests.post(url_post, headers=headers, data=body)
	assert reqs.status_code == 201
	response = reqs.json()

	item_response(response)

	data = response.get('data')
	# print(type(data))
	id_appointment = data['id']

	body['datetime'] = "2022-12-12T16:39:00"
	reqs = requests.post(url_post, headers=headers, data=body)
	assert reqs.status_code == 201
	response = reqs.json()
	item_response(response)
	data = response.get('data')
	id_appointment_2 = data['id']
	
	reqs = requests.post(url_post, headers=headers, data=body)
	assert reqs.status_code == 400
	
	# del data['id']
	assert body['doctor_id'] == data['doctor_id']
	assert body['patient_id'] == data['patient_id']


def test_get():
	global token
	url_get =  F'{url_base}appointments'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.get(url_get, headers= headers)

	assert reqs.status_code == 200
	response = reqs.json()

	item_response(response)


def test_get_by_id():
	global token, id_appointment, body

	url_get =  F'{url_base}appointments/{id_appointment}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.get(url_get, headers= headers)
	assert reqs.status_code == 200 
	response = reqs.json()
	
	item_response(response)
	data = response.get('data')

	assert body['doctor_id'] == data['doctor_id']
	assert body['patient_id'] == data['patient_id']


def test_put_by_id():
	global token, id_appointment, body
	body_put = {
		'doctor_id'		: id_doctor,
		'patient_id' 	: id_patient,
		'datetime' 		: "2022-12-12T23:20:00"
	}
	url_put =  F'{url_base}appointments/{id_appointment}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.put(url_put, headers= headers, data= body_put)
	assert reqs.status_code == 400 

	body_put['datetime'] = "2022-12-12T16:39:00"
	reqs = requests.put(url_put, headers= headers, data= body_put)
	assert reqs.status_code == 400 

	body_put['diagnose'] 	= "nothing" 
	body_put['notes'] 		= "Nice"
	body_put['datetime'] 	= "2022-12-12T21:00:00"
	body_put['status'] 		= "DONE"
	
	reqs = requests.put(url_put, headers= headers, data= body_put)
	assert reqs.status_code == 200 
	response = reqs.json()
	
	item_response(response)
	data = response.get('data')

	assert body_put['patient_id'] == data['patient_id']
	assert body_put['doctor_id'] == data['doctor_id']
	assert body_put['diagnose'] == data['diagnose']
	assert body_put['notes'] == data['notes']
	# assert body_put['datetime'] == data['datetime']
	assert body_put['status'] == data['status']


def test_delete_patient():
	global token, id_patient

	url_get =  F'{url_base}patients/{id_patient}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.delete(url_get, headers= headers)
	assert reqs.status_code == 204 

def test_delete_docter():
	global token, id_doctor

	url_get =  F'{url_base}doctors/{id_doctor}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.delete(url_get, headers= headers)
	assert reqs.status_code == 204 
	
def test_delete():
	global token, id_appointment, id_appointment_2

	url_get =  F'{url_base}appointments/{id_appointment}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.delete(url_get, headers= headers)
	assert reqs.status_code == 204 

	url_get =  F'{url_base}appointments/{id_appointment_2}'
	reqs = requests.delete(url_get, headers= headers)
	assert reqs.status_code == 204 

