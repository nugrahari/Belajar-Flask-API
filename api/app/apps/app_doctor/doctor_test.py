import os
import requests

url_base = 'http://127.0.0.1:5000/'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjU3MDAwOTUwLCJqdGkiOiJlZDkzN2FlOC1jMDhmLTQ4MDMtYTU4Mi1jMGNhNDQ4ZTcwYjciLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoxMCwidXNlcm5hbWUiOiJ6dWJhaXIifSwibmJmIjoxNjU3MDAwOTUwfQ.Wn3hI0AvTaFQJcWiAj8RwGV4QCsl9-juVCjV1k-a4RY'
# token = os.getenv('API_TOKEN')
id_doctor = None
body = {}


def item_response(response):
	assert 'message' in response
	assert 'data' in response


def test_post():
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
		'work_end_time': '21:00:59'
	}
	reqs = requests.post(url_post, headers=headers, data=body)

	assert reqs.status_code == 201
	response = reqs.json()

	item_response(response)

	data = response.get('data')
	# print(type(data))
	id_doctor = data['id']
	
	del data['id']
	assert body['username'] == data['username']
	assert body['name'] == data['name']
	assert body['gender'] == data['gender']
	assert body['work_start_time'] == data['work_start_time']
	assert body['work_end_time'] == data['work_end_time']


def test_get():
	global token
	url_get =  F'{url_base}doctors'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.get(url_get, headers= headers)

	assert reqs.status_code == 200
	response = reqs.json()

	item_response(response)


def test_get_by_id():
	global token, id_doctor, body

	url_get =  F'{url_base}doctors/{id_doctor}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.get(url_get, headers= headers)
	assert reqs.status_code == 200 
	response = reqs.json()
	
	item_response(response)
	data = response.get('data')

	assert body['username'] == data['username']
	assert body['name'] == data['name']
	assert body['gender'] == data['gender']
	assert body['work_start_time'] == data['work_start_time']
	assert body['work_end_time'] == data['work_end_time']


def test_put_by_id():
	global token, id_doctor, body
	body_put = {
		'username' 	: "aaaaaa",
		'name'		: "Hati Septia",
		'gender'	: "Perempuan",
		'work_start_time': '07:44:30',
		'work_end_time': '21:30:20'
	}
	url_put =  F'{url_base}doctors/{id_doctor}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.put(url_put, headers= headers, data= body_put)
	assert reqs.status_code == 200 

	response = reqs.json()
	
	item_response(response)
	data = response.get('data')

	assert body_put['username'] == data['username']
	assert body_put['name'] == data['name']
	assert body_put['gender'] == data['gender']
	assert body_put['work_start_time'] == data['work_start_time']
	assert body_put['work_end_time'] == data['work_end_time']

	
def test_delete():
	global token, id_doctor

	url_get =  F'{url_base}doctors/{id_doctor}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.delete(url_get, headers= headers)
	assert reqs.status_code == 204 
