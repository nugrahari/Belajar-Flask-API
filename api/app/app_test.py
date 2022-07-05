import os
import requests

url_base = 'http://127.0.0.1:5000/'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjU2OTA2NjI1LCJqdGkiOiI5NDUzZDlmYi0yMjg5LTQ3MDktYWQ0Zi1lODdjOGQ5YjE5MjQiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoxMCwidXNlcm5hbWUiOiJ6dWJhaXIifSwibmJmIjoxNjU2OTA2NjI1LCJleHAiOjE2NTY5OTMwMjV9.GzslEhheqQrP6u82JaUo5KAR8UXkaQPHOc9Z7cmF6F4'

def test_root():
	headers = {"Authorization": F"Bearer {token}"}
	requests_get = requests.get(url_base, headers=headers)
	assert requests_get.status_code == 200
	data = requests_get.json()

	assert 'message' in data
	title = data.get('title')
	assert "SRS Delman" == title

	


