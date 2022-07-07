import os
import time
import logging
import requests
from google.cloud import bigquery

from dotenv import load_dotenv
load_dotenv()

api_host : str = os.getenv('CRON_API_HOST')
token 	 : str = os.getenv('CRON_API_TOKEN')
api_port : str = os.getenv('CRON_API_PORT')
time_wait: int = int(os.getenv('CRON_TIME_WAIT'))

def update_now():
	url_get = F'http://{api_host}:{api_port}/patients'
	headers = {"Authorization": F"Bearer {token}"}
	requests_get = requests.get(url_get, headers=headers).json()

	client = bigquery.Client()
	query_job = client.query(
	    """
	    SELECT
	      *
	    FROM `delman-interview.interview_mock_data.vaccine-data`
	    LIMIT 100"""
	)

	results = query_job.result() 
	for row in results:
		for data in requests_get['data']:
			if str(data['no_ktp']) == str(row[0]):
				body_data = {
					"vaccine_type" : row[1],
					"vaccine_count": row[2]
				}
				requests_put = requests.put(F"{url_get}/{data['id']}", data = body_data, headers=headers)
				break

if __name__ == '__main__':
	while True:		
		logging.warning('Executing..!')
		update_now()
		logging.warning('Waiting for execute..!')
		time.sleep(time_wait)
