from test_server.utils.responseJSON import *
import configparser


def set_variable(title, dict_s):
	try:
		config = configparser.ConfigParser()
		path = r'C:\test_server\test\test_server\API_request\table_s\variable.ini'
		config.read(path, encoding="utf-8")
		if type(dict_s) != dict:
			return responseJSON_0(msg='参数不是json格式！', data=dict_s)
		for i in dict_s:
			config.set(title, i, str(dict_s[i]))
		if config.write(open(path, 'w')) == None:
			return responseJSON_1()
		else:
			return responseJSON_0(msg='其他异常')
	except Exception as ERR:
		return responseJSON_0(msg='set_variable function error', data=ERR)


if __name__ == '__main__':
	print(set_variable('game0', {'name': 'ahua'}))


def get_variable(title, values):
	config = configparser.ConfigParser()
	path = r'C:\test_server\test\test_server\API_request\table_s\variable.ini'
	config.read(path, encoding="utf-8")
	return config.get(title, values)


if __name__ == '__main__':
	get_variable('game0', 'user_id')
