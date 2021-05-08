
from test_server.API_request.util.run_sql import run_sql
def get_parameter(port_path):
	sql = '''
	SELECT parameter_key,parameter_value FROM port_parameter WHERE port_path = '{}';
	'''.format(port_path)
	data = run_sql(sql)
	re_data = dict()
	for i in data:
		re_data[i['parameter_key']] = i['parameter_value']
	return re_data
if __name__ == '__main__':
	print(get_parameter('/api/login/wllogin'))


'''
[{'parameter_key': 'username', 'parameter_value': 'XLM0042'}, 
 {'parameter_key': 'pwd', 'parameter_value': '123456'}, 
 {'parameter_key': 'cToken', 'parameter_value': '4931374c-ba4d-4127-91c4-036e891fa1bd'}, 
 {'parameter_key': 'captcha', 'parameter_value': '6666'}, 
 {'parameter_key': 'isLongLogin', 'parameter_value': '0'}]
'''

