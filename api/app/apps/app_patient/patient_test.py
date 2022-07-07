import os
import requests

url_base = 'http://127.0.0.1:5000/'
token = None
id_patient = None
body = {}


def item_response(response):
	assert 'message' in response
	assert 'data' in response


def test_post(admin1_token):
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
	
	del data['id']
	assert body['no_ktp'] == data['no_ktp']
	assert body['address'] == data['address']
	assert body['name'] == data['name']
	assert body['gender'] == data['gender']
	assert body['vaccine_type'] == data['vaccine_type']
	assert body['vaccine_count'] == data['vaccine_count']


def test_get():
	global token
	url_get =  F'{url_base}patients'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.get(url_get, headers= headers)

	assert reqs.status_code == 200
	response = reqs.json()

	item_response(response)


def test_get_by_id():
	global token, id_patient, body

	url_get =  F'{url_base}patients/{id_patient}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.get(url_get, headers= headers)
	assert reqs.status_code == 200 
	response = reqs.json()
	
	item_response(response)
	data = response.get('data')

	assert body['no_ktp'] == data['no_ktp']
	assert body['address'] == data['address']
	assert body['name'] == data['name']
	assert body['gender'] == data['gender']
	assert body['vaccine_type'] == data['vaccine_type']
	assert body['vaccine_count'] == data['vaccine_count']


def test_put_by_id():
	global token, id_patient, body
	body_put = {
		'name'		: "Solehudan",
		'no_ktp' 	: "8795784567456",
		'address' 	: "Langen Kota",
		'gender'	: "Perempuan",
		'birthdate'	: "1989-06-03",
		'vaccine_type': 'Sinofakses',
		'vaccine_count': 3
	}
	url_put =  F'{url_base}patients/{id_patient}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.put(url_put, headers= headers, data= body_put)
	assert reqs.status_code == 200 

	response = reqs.json()
	
	item_response(response)
	data = response.get('data')

	assert body_put['no_ktp'] == data['no_ktp']
	assert body_put['address'] == data['address']
	assert body_put['name'] == data['name']
	assert body_put['gender'] == data['gender']
	assert body_put['vaccine_type'] == data['vaccine_type']
	assert body_put['vaccine_count'] == data['vaccine_count']

	
def test_delete():
	global token, id_patient

	url_get =  F'{url_base}patients/{id_patient}'
	headers = {"Authorization": F"Bearer {token}"}
	reqs = requests.delete(url_get, headers= headers)
	assert reqs.status_code == 204 
