import requests,json

def jsonAPI(url,path,re_data):

	'''
	:param user_id:
	:param new_mobile:
	:return:
	'''
	headers = {
		"Content-Type": "application/json; charset=UTF-8"
	}
	url = url + path
	try:
		response = requests.post(url, data=json.dumps(re_data), headers=headers)
		return response.json()
	except:
		return 'jsonAPI：异常'
