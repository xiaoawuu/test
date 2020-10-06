import datetime, time
from test_server.timedTask.utils.WriteLog import writeLog
from test_server.data.sql import sql_select, sql_exec


def IOSRechargeRecord():
	'''
	检测IOS充值未处理的订单
	:return:
	'''
	try:
		re_data = sql_select("SELECT order_sn FROM apple_pay_callback_log WHERE status = 0 GROUP BY order_sn;")
		print(re_data)
		if re_data != []:
			writeLog("IOS充值未成功订单", re_data)
	except Exception as Err:
		writeLog("IOSRechargeRecord:异常", Err)


# IOSRechargeRecord()


def Complain():
	yesterday = datetime.date.today() + datetime.timedelta(-1)
	startTime = '{} 00:00:00'.format(yesterday)
	endTime = '{} 23:59:59'.format(yesterday)
	startTimestamp = int(time.mktime(time.strptime(startTime, "%Y-%m-%d %H:%M:%S")))
	endTimestamp = int(time.mktime(time.strptime(endTime, "%Y-%m-%d %H:%M:%S")))
	# print(startTime)
	try:
		re_data = sql_select(
			"SELECT COUNT(*) FROM biz_complain WHERE create_time BETWEEN '{}' AND '{}';".format(startTime, endTime))
		re_data1 = sql_select(
			"SELECT COUNT(*) FROM biz_report WHERE create_time BETWEEN '{}' AND '{}';".format(startTime, endTime))

		print(re_data[0][0])
		if re_data[0][0] != 0 or re_data1[0][0] != 0:
			writeLog("用户投诉", "昨天有{}位用户发起投诉,{}用户发起举报！".format(re_data[0][0], re_data1[0][0]))
	except Exception as Err:
		writeLog("Complain:异常", Err)

# Complain()
IOSRechargeRecord()