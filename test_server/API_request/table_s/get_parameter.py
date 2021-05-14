
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

CREATE TABLE `port_parameter` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `port_path` varchar(255) NOT NULL COMMENT '接口路径',
  `parameter_key` varchar(255) NOT NULL COMMENT '请求参数_键',
  `parameter_value` varchar(255) NOT NULL COMMENT '请求参数_值',
  `system_name` char(64) NOT NULL COMMENT '系统',
  `request_way` char(64) NOT NULL COMMENT '请求方式',
  `test_function` varchar(255) NOT NULL COMMENT '参数方法名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='接口请求参数';

.


CREATE TABLE `request_port` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `port_path` varchar(255) NOT NULL COMMENT '接口路径',
	`request_data`varchar(255) NOT NULL COMMENT '接口请求值',
	`response_data`varchar(255) NOT NULL COMMENT '接口返回值',
	`test_function` varchar(255) NOT NULL COMMENT '参数方法名',
	`error_data` varchar(255) NOT NULL COMMENT '错误响应值',
  PRIMARY KEY (`id`)
)CHARSET=utf8 COMMENT='接口请求参数';

'''