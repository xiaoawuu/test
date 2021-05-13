from test_server.API_request.util.run_sql import run_sql

def get_request_port():
	sql = '''
	SELECT * FROM request_port;
	'''
	data = run_sql(sql)
	return data

if __name__ == '__main__':
	print(get_request_port())

