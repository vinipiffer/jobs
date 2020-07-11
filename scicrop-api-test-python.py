import requests, json, datetime

def loadjson():
	with open('/Users/viniciuspiffer/Desktop/resume.json') as file:
		resume = json.load(file)
	return resume

def main():
	resume = loadjson()
	start_date = datetime.datetime(2020, 7, 11, 18, 0, 0).strftime("%s")
	begin_date = datetime.datetime(2019, 2, 4, 19, 0, 0).strftime("%s")
	end_date = datetime.datetime(2020, 8, 21, 23, 0, 0).strftime("%s")

	resume['start_date'] = int(start_date)
	resume['degrees'][0]['begin_date'] = int(begin_date)
	resume['degrees'][0]['end_date'] = int(end_date)

	url = ('https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume')
	head = {'content-type' : 'application/json'}

	try:
		response = requests.post(url, headers=head, json=resume)
		if response.status_code == 200:
			print(response.status_code)
			print(response.content)
			print(resume)
	except:
		print('Error requesting\n')
		print(response.status_code)
		print(response.content)
	finally:
		print('Process completed successfully')

if __name__ == '__main__':
	main()