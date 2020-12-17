from jy_server.Data.sysLog import insert
from test_server.data.sql import sql_exec, sql_select
from test_server.utils.responseJSON import responseJSON_1, responseJSON_0


def Logout_user(mobile):
	try:
		user_id = sql_select("SELECT id FROM biz_user WHERE mobile = {}".format(mobile))
		if user_id == []:
			return responseJSON_0('用户不存在！')
		sql_exec("exec RemoveUserByMobile '{}';".format(mobile))
		insert(user_id[0][0], 'Logout_user', '账户注销')
		return responseJSON_1('注销成功', mobile)
	except Exception as error:
		return responseJSON_0('deleteUser异常', error)


# if __name__ == '__main__':
# 	print(Logout_user('15089671800'))
