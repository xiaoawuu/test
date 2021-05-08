from test_server.data.mysqls import Data
def	run_sql(sql):
	sql_ = Data().query
	return sql_('localhost',sql)

if __name__ == '__main__':
	print(run_sql("SELECT parameter_key,parameter_value FROM port_parameter WHERE port_path = '/api/login/wllogin';"))

