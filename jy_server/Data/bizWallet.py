from test_server.utils.responseJSON import responseJSON_1, responseJSON_0
from test_server.data.sql import sql_select, sql_exec


def getBizWallet(mobile):
	try:
		sql = "SELECT currency,user_id FROM biz_wallet A JOIN biz_user B ON A.user_id = B.id WHERE B.mobile = N'{}';".format(
			mobile)
		sql = sql_select(sql)
		return responseJSON_1('查询成功', sql)
	except Exception as error:
		return responseJSON_0('getBizWallet异常', error)


