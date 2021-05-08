from test_server.API_request.util.responseJSON import *
import requests


def fron_data(url, payload):
	try:
		if type(payload) != dict:
			return responseJSON_0(msg='请求参数非正确的json值！')
		headers = {
			'Cookie': 'SESSION=83325336-931c-4191-a1ec-df3cbd4667ca'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		return response.text
		# print(response.text)
	except Exception as ERR:
		print(responseJSON_0(msg='fron_data方法异常！',data=ERR))

if __name__ == '__main__':
	dict_s = {'username': 'XLM0042', 'pwd': '123456', 'cToken': '4931374c-ba4d-4127-91c4-036e891fa1bd', 'captcha': '6666', 'isLongLogin': '0'}
	fron_data('http://wl.test.zyb56.cn/api/login/wllogin',dict_s)
