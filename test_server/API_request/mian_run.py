from test_server.API_request.data.get_parameter import get_parameter
from test_server.API_request.util.request_fun import fron_data

import json
def	get_request_data(port_path):
	url = 'http://wl.test.zyb56.cn' + port_path
	return fron_data(url,get_parameter(port_path))




if __name__ == '__main__':
	a = get_request_data('/api/login/wllogin')
	print(a)
	print(type(a))
	print(type(json.loads(a)))
	print(len(a))