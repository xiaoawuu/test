from test_server.API_request.table_s.get_parameter import get_parameter
from test_server.API_request.table_s.get_request_port import get_request_port
from test_server.API_request.test_case.test_function import *
from test_server.API_request.util.request_fun import fron_data

from test_server.API_request.util.responseJSON import *



def main_run():
	parameter_data = get_request_port()
	# print(parameter_data)
	if len(parameter_data) == 0:
		return responseJSON_0(msg='接口数量为空',data='parameter_data={}'.format(parameter_data))
	for i in parameter_data:
		url = 'http://wl.test.zyb56.cn' + i['port_path']
		response_data = fron_data(url, get_parameter(i['port_path']))
		if i['test_function'] != None:
			eval(i['test_function'])


if __name__ == '__main__':
	main_run()
