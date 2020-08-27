
from test_server.requestPort import requestsPort
def getToken(user,pwd):
	url = '/api/captcha/captcha'
	token = requestsPort(url,{'':''})['data']['cToken']
	wlLogin = {
	  "username": user,
	  "pwd": pwd,
	  "cToken": token,
	  "captcha": "6666",
	  "isLongLogin": "0"
	}
	return requestsPort('/api/login/wllogin',wlLogin)
# print(getToken('HGW0010','123456'))