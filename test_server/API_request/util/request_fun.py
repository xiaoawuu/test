from test_server.API_request.util.parameterization import parameterization_str
from test_server.API_request.util.responseJSON import *
from test_server.API_request.util.print_ import *
import requests,json

import requests



def test_port_from_data(url, payload):
	try:
		if type(payload) != dict:
			return responseJSON_0(msg='请求参数非正确的json值！')
		headers = {
			'Cookie': 'SESSION=83325336-931c-4131-a1ec-df3cbd4467ca'
		}
		s = requests.session()
		s.proxies = {"https": "wl.zyb56.com:8080", "http": "wl.test.zyb56.cn:80", }
		s.headers = headers
		s.get(url)

		response = requests.request("POST", url, headers=headers, data=payload)
		if response.status_code == 200:
			return responseJSON_1(data=response.json())
		
		return responseJSON_0(data=response)
	except Exception as ERR:
		return responseJSON_0(msg='test_port_from_data方法异常！', data=ERR)

if __name__ == '__main__':
	print(test_port_from_data('http://wl.test.zyb56.cn/api/captcha/captcha',{}))

def fron_data(url, payload):
	try:
		if type(payload) != dict:
			return responseJSON_0(msg='请求参数非正确的json值！')
		headers = {
			'Cookie': 'SESSION=83325336-931c-4191-a1ec-df3c554667ca'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		if response.status_code != 200:
			return responseJSON(code=response.status_code, msg='接口请求响应代码错误！', data=response.text)
		'''
		请求参数和响应需要写库
		'''
		return response.json()
	except Exception as ERR:
		return responseJSON_0(msg='fron_data方法异常！', data=ERR)


# if __name__ == '__main__':
	# dict_s = {'username': 'XLM0042', 'pwd': '123456', 'cToken': '4931374c-ba4d-4127-91c4-036e891fa1bd',
	# 		  'captcha': '6666', 'isLongLogin': '0'}
	# print(fron_data('http://wl.test.zyb56.cn/api/login/wllogin', dict_s))
	# print(fron_data('http://wl.test.zyb56.cn/api/message/getRead',{"wlToken": "wl_token_1621147454676940"}))
