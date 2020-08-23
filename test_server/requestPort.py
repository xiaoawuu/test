import requests
from test_server import return_s
def	requestsPort(re_url,payload,):
	url = 'http://wl.test.zyb56.cn'
	headers = {
		'Cookie': 'SESSION=0d5284e2-db64-45f7-947d-a4e315d9f6da'
	}
	files = []
	url = url + str(re_url)
	try:
		response = requests.request("POST", url, headers=headers, data=payload, files=files)
	except:
		return response.json()
	else:
		return response.json()

def	requestsPorts(re_url,payload,frequency=1):
	url = 'http://wl.test.zyb56.cn'
	headers = {
		'Cookie': 'SESSION=0d5284e2-db64-45f7-947d-a4e315d9f6da'
	}
	files = []
	i = 0
	url = url + str(re_url)
	succeed = 0
	error = 0
	try:
		while i < frequency:
			i += 1
			response = requests.request("POST", url, headers=headers, data=payload, files=files)
			if response.json()['code'] == 0:
				succeed += 1
			else:
				error += 1
	except:
		return response.json()
	else:
		return response.json()