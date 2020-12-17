from jy_server.Data.bizVipRecord import setBizVipRecord
from jy_server.Data.bizWallet import getBizWallet
from jy_server.Data.sysLog import insert
from jy_server.Modules.UserStatus import userStatus, vipStatus
from test_server.data.sql import sql_exec, sql_select
from test_server.utils.responseJSON import responseJSON_1, responseJSON_0

import time


def addMoney(mobile, money):
	setMealList = [0.1, 0.5, 1, 3, 6]
	user_start = userStatus(mobile)
	if user_start['code'] == 0:
		return user_start
	if float(money) <= 6:
		if float(money) not in setMealList:
			return responseJSON_0("充值月份不在范围！")
		vip_status = vipStatus(mobile)
		status = vip_status['code']
		if status == 0:
			return vip_status
		if float(money) == 0.1:
			user_id = sql_select("SELECT id FROM biz_user WHERE mobile = {}".format(mobile))[0][0]
			if status == 2:
				user_id = vip_status['data'][0]
				validTime = vip_status['data'][1]
				timeArray = time.strptime(validTime, "%Y-%m-%d %H:%M:%S")
				timeStamp = int(time.mktime(timeArray))
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(864000 * money + timeStamp))
				return setBizVipRecord(user_id, validTime, money)
			else:
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(864000 * money + int(time.time())))
			return setBizVipRecord(user_id, validTime, money)
		# 未开通
		if status == 1:
			user_id = sql_select("SELECT id FROM biz_user WHERE mobile = {}".format(mobile))[0][0]
			validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * money + int(time.time())))
			return setBizVipRecord(user_id, validTime, money)

		# 已开通
		elif status == 2:
			user_id = vip_status['data'][0]
			validTime = vip_status['data'][1]
			timeArray = time.strptime(validTime, "%Y-%m-%d %H:%M:%S")
			timeStamp = int(time.mktime(timeArray))
			validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * money + timeStamp))
			return setBizVipRecord(user_id, validTime, money)

		# 已过期
		elif status == 3:
			user_id = vip_status['data'][0]
			validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * money + int(time.time())))
			return setBizVipRecord(user_id, validTime, money)
	else:
		money = int(money)
		if money > 4000 or money < 10:
			return responseJSON_0('充值失败！', '充值金额范围10~4000')
		sql_exec("exec GiveMeTheMoney %s,%d;" % (mobile, money))
		bizWallet = getBizWallet(mobile)
		insert(bizWallet['data'][0][1], 'setBizVipRecord', 'TEST:充值{}个聚源币'.format(money))
		if bizWallet['code'] == 0:
			return bizWallet
		return responseJSON_1('充值成功！', '当前余额为{}币'.format(bizWallet['data'][0][0]))

