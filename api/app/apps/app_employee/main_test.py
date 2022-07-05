import os
import requests

url_base = 'http://127.0.0.1:5000/'
id_employee = None
token = None
body = {}


def test_login():
	global token

	url_login = F'{url_base}login'
	reqs = requests.post(url_login, data={'username':'zubair', 'password':'abcd1234'})
	assert reqs.status_code == 200
	response = reqs.json()

	assert 'message' in response
	assert 'access_token' in response
	assert 'refresh_token' in response

	token = response.get('access_token')


def item_response(response):
	assert 'message' in response
	assert 'data' in response


def test_post():
	global token, id_employee, body
	url_post =  F'{url_base}employees'
	headers = {"Authorization": F"Bearer {token}"}

	body = {
		'username' 	: "mustofa",
		'name'		: "Hata Rajasa",
		'password' 	: "maryati",
		'gender'	: "laki-laki",
		'birthdate'	: "1988-02-25"
	}
	reqs = requests.post(url_post, headers=headers, data=body)

	assert reqs.status_code == 201
	response = reqs.json()

	item_response(response)

	data = response.get('data')
	# print(type(data))
	id_employee = data['id']
	
	del data['id']
	assert body['username'] == data['username']
	assert body['name'] == data['name']
	assert body['gender'] == data['gender']
	assert body['gender'] == data['gender']


def test_get():
	global token
	url_get =  F'{url_base}employees'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.get(url_get, headers= headers)

	assert reqs.status_code == 200
	response = reqs.json()

	item_response(response)


def test_get_by_id():
	global token, id_employee, body

	url_get =  F'{url_base}employees/{id_employee}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.get(url_get, headers= headers)
	assert reqs.status_code == 200 
	response = reqs.json()
	
	item_response(response)
	data = response.get('data')

	assert body['username'] == data['username']
	assert body['name'] == data['name']
	assert body['gender'] == data['gender']
	assert body['gender'] == data['gender']


def test_put_by_id():
	global token, id_employee, body
	body_put = {
		'username' 	: "aaaaaa",
		'name'		: "Hati Septia",
		'gender'	: "Perempuan",
	}
	url_put =  F'{url_base}employees/{id_employee}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.put(url_put, headers= headers, data= body_put)
	assert reqs.status_code == 200 

	response = reqs.json()
	
	item_response(response)
	data = response.get('data')

	assert body_put['username'] == data['username']
	assert body_put['name'] == data['name']
	assert body_put['gender'] == data['gender']

	
def test_delete():
	global token, id_employee

	url_get =  F'{url_base}employees/{id_employee}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.delete(url_get, headers= headers)
	assert reqs.status_code == 204 
