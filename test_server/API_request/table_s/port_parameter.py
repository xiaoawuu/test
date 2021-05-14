from test_server.API_request.util.run_sql import run_sql
from test_server.utils.responseJSON import *


def add(port_path, parameter_key, parameter_value):
	try:
		insert_sql = '''
		INSERT INTO port_parameter (port_path, parameter_key, parameter_value) VALUES ('{}', '{}', '{}');
		'''.format(port_path, parameter_key, parameter_value)
		select_sql = '''
		SELECT COUNT(1) as count FROM port_parameter WHERE port_path = '{}' AND parameter_key = '{}';
		'''.format(port_path, parameter_key)
		update_sql = '''
		UPDATE port_parameter SET parameter_value = '{}' WHERE port_path = '{}' AND parameter_key = '{}';
		'''.format(parameter_value, port_path, parameter_key)

		re_data = run_sql(select_sql)
		if re_data[0]['count'] == 1:
			response = run_sql(update_sql)
			if response == ():
				return responseJSON_1(msg = '更新成功')
		elif re_data[0]['count'] == 0:
			response = run_sql(insert_sql)
			if response == ():
				return responseJSON_1(msg = '新增成功')
		else:
			return responseJSON_0(msg='port_parameter.add：error_data')
	except Exception as ERR:
		return responseJSON_0(msg='port_parameter.add异常', data=ERR)


if __name__ == '__main__':
	print(add('/api/login/wllogin', 'captchaaaa', '6666'))

'''
CREATE TABLE `port_parameter` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `port_path` varchar(255) NOT NULL COMMENT '接口路径',
  `parameter_key` varchar(255) NOT NULL COMMENT '请求参数_键',
  `parameter_value` varchar(255) NOT NULL COMMENT '请求参数_值',
  `system_name` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '系统',
  `request_way` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '请求方式',
  `test_function` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '参数方法名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='接口请求参数';
'''
