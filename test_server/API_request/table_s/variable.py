# coding=utf-8

from test_server.API_request.util.responseJSON import *
from test_server.API_request.util.print_ import *
import configparser

def set_variable(dict_s,title='global'):
	try:
		config = configparser.ConfigParser()
		path = r'C:\test_s\test_server\API_request\table_s\variable.ini'
		config.read(path, encoding="GBK")
		if type(dict_s) != dict:
			return responseJSON_0(msg='参数不是json格式！', data=dict_s)
		if not config.has_section(title):
			config.add_section(title)
		for i in dict_s:
			config.set(title, i.strip(), str(dict_s[i]))
		if config.write(open(path, 'w')) is None:
			return responseJSON_1(msg='变量设置成功！')
		else:
			return responseJSON_0(msg='set_variable update error')
	except FileNotFoundError as ERR:
		return responseJSON_0(msg='文件路径打不开！', data=ERR)
	except Exception as ERR:
		return responseJSON_0(msg='set_variable function error', data=ERR)


if __name__ == '__main__':
	# print(set_variable({'cToken': 'bc19d1f2-ff35-4d31-9ef5-ffd48d71398d'},'global'))
	print(set_variable({'wlToken ': None},'global'))


def get_variable(title, values):
	title = 'global'
	try:
		config = configparser.ConfigParser()
		path = r'C:\test_s\test_server\API_request\table_s\variable.ini'
		config.read(path, encoding="GBK")
		if config.has_section(title) and config.has_option(title, values):
			return responseJSON_1(msg='获取成功', data=config.get(title, values))
		return responseJSON_0(msg='变量不存在！')
	except FileNotFoundError as ERR:
		return responseJSON_0(msg='文件路径打不开！', data=ERR)
	except Exception as ERR:
		return responseJSON_0(msg='get_variable其他异常！', data=ERR)


def transition_variable(dict_, variable_list):
	"""
	设置变量
	缺少正则表达式,容错率低
	:param variable_list:
	:param dict_:
	:return:
	"""
	try:
		if type(dict_['data']) != dict:
			return dict_
		if type(dict_) != dict:
			return responseJSON_0(msg='参数不是json类型!',data=dict_)
		if variable_list == '':
			return responseJSON_1(msg='变量设置成功!')
		global key_s, dict_str
		for transition in variable_list.split(','):
			dict_str = 'dict_'
			for i in transition.split('.'):
				if '=' in i:
					key_s = i.split('=')[0]
					continue
				dict_str = dict_str + '[' + '"' + i + '"' + ']'
				variable = set_variable({key_s:eval(dict_str)})
				if variable['code'] == 0:
					return variable
		return responseJSON_1(msg='获取成功',data={key_s:eval(dict_str)})
	except KeyError as ERR:
		return responseJSON_0(msg='变量路径错误', data=ERR)
	except Exception as ERR:
		return responseJSON_0(msg='transition_variable fun error', data=ERR)




if __name__ == '__main__':
	dict_s = {'msg': None, 'code': 1, 'data': {
		'img': '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',
		'cToken': '877350a7-d563-4338-8cca-26e4c9189977', 'captcha': 'gxfg'}}

	# print(transition_variable(dict_s, 'cToken = responses.data.cToken,captcha = responses.data.captcha'))

# if __name__ == '__main__':
# 	print(get_variable('/api/captcha/captcha', 'gender'))
