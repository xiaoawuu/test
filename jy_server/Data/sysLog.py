from test_server.utils.responseJSON import responseJSON_1, responseJSON_0
from test_server.data.sql import sql_select, sql_exec

def	insert(user_id,module,describe):
	try:
		sql = "INSERT INTO sys_log (user_id,[module],[describe]) VALUES ('{}','{}','{}');".format(user_id, module,
																								  describe)
		sql_exec(sql)
		return responseJSON_1('更新成功')
	except Exception as error:
		responseJSON_0('更新失败',error)
