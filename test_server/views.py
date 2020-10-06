from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bin.test_port.select_port import models
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
import json
import sys, corsheaders

sys.path.append(r'C:\test_server\bin')

from django.shortcuts import render, HttpResponse
import json
from test_server.data import sql, mysqls
from test_server.utils import is_int
import time


def addMoneys(request):
	return render(request, 'config.html')


def addMoney(request):
	if request.method == "POST":
		mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
		money = json.loads(request.body.decode().replace("'", "\"")).get('money')
		setMealList = [0.5,1,3,6]
		if float(money) in setMealList:
			money = float(money)
			is_mobile = sql.sql_select("SELECT status FROM biz_user WHERE mobile = '{}';".format(mobile))
			if is_mobile == []:
				return HttpResponse(json.dumps({"code": 0, "msg": "用户不存在！", "data": ""}))
			if is_mobile[0][0] != 4:
				return HttpResponse(json.dumps({"code": 0, "msg": "用户还未完成认证！", "data": ""}))
			if float(money) not in [0.5, 1, 3, 6]:
				return HttpResponse(json.dumps({"code": 0, "msg": "充值失败,充值月份不在范围！", "data": ""}))
			is_true = sql.sql_select(
				"SELECT A.id,B.expire_time FROM biz_user A JOIN biz_vip_record B ON A.id = B.user_id WHERE sex=1 AND A.mobile='{}';".format(
					mobile))
			if is_true == []:
				user_id = sql.sql_select("SELECT id FROM biz_user WHERE mobile = '{}';".format(mobile))[0][0]
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * money + int(time.time())))
				sql.sql_exec(
					"INSERT INTO biz_vip_record (user_id,expire_time) VALUES ({},'{}');"
					"update biz_user set is_vip=1 where id={};".format(user_id, validTime, user_id))
				return HttpResponse(
					json.dumps({"code": 1, "msg": "未充值VIP！", "data": "user_id: {},会员时间：{}".format(user_id, validTime)}))
			user_id = is_true[0][0]
			timeArray = time.strptime(is_true[0][1], "%Y-%m-%d %H:%M:%S")
			timeStamp = int(time.mktime(timeArray))

			if timeStamp > int(time.time()):
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * money + timeStamp))
				sql.sql_exec("UPDATE biz_vip_record SET expire_time='{}' WHERE user_id= {};"
							 "update biz_user set is_vip=1 where id={};".format(validTime, user_id, user_id))
				return HttpResponse(json.dumps({"code": 1, "msg": "未过期！", "data": "{}".format(validTime)}))

			if timeStamp < int(time.time()):
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * money + int(time.time())))
				sql.sql_exec(
					"UPDATE biz_vip_record SET expire_time='{}' WHERE user_id= {};"
					"update biz_user set is_vip=1 where id={};".format(validTime, user_id, user_id))
				return HttpResponse(json.dumps({"code": 1, "msg": "过期！", "data": ""}))

		else:
			if money == "" or mobile == "":
				return HttpResponse(json.dumps({"code": 0, "msg": "金额或金额类型异常", "data": ""}))
			if type(money) != int:
				money = int(money)
			if is_int.is_number(money) or type(money) != int:
				return HttpResponse(json.dumps({"code": 0, "msg": "金额或金额类型异常", "data": ""}))
			if money > 4000 or money < 1:
				return HttpResponse(json.dumps({"code": 0, "msg": "金额充值范围1~4000币", "data": ""}))
			is_mobile = sql.sql_select("SELECT status FROM biz_user WHERE mobile = '{}';".format(mobile))
			if is_mobile == []:
				return HttpResponse(json.dumps({"code": 0, "msg": "用户不存在！", "data": ""}))
			if is_mobile[0][0] != 4:
				return HttpResponse(json.dumps({"code": 0, "msg": "用户还未完成认证！", "data": ""}))

			return HttpResponse(json.dumps({"code": 1, "msg": "充值成功！", "data": "当前账户余额:{}"}))
	else:
		return HttpResponse(json.dumps({"code": 0, "msg": "请使用POST请求！", "data": ""}))


def addMembers(request):
	try:
		if request.method == "POST":
			mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
			month = json.loads(request.body.decode().replace("'", "\"")).get('month')
			if month == "" or mobile == "":
				return HttpResponse(json.dumps({"code": 0, "msg": "金额或金额类型异常", "data": ""}))
			is_mobile = sql.sql_select("SELECT status FROM biz_user WHERE mobile = '{}';".format(mobile))
			if is_mobile == []:
				return HttpResponse(json.dumps({"code": 0, "msg": "用户不存在！", "data": ""}))
			if is_mobile[0][0] != 4:
				return HttpResponse(json.dumps({"code": 0, "msg": "用户还未完成认证！", "data": ""}))
			if float(month) not in [0.5, 1, 3, 6]:
				return HttpResponse(json.dumps({"code": 0, "msg": "充值失败,充值月份不在范围！", "data": ""}))
			is_true = sql.sql_select(
				"SELECT A.id,B.expire_time FROM biz_user A JOIN biz_vip_record B ON A.id = B.user_id WHERE sex=1 AND A.mobile='{}';".format(
					mobile))
			if is_true == []:
				user_id = sql.sql_select("SELECT id FROM biz_user WHERE mobile = '{}';".format(mobile))[0][0]
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * month + int(time.time())))
				sql.sql_exec(
					"INSERT INTO biz_vip_record (user_id,expire_time) VALUES ({},'{}');"
					"update biz_user set is_vip=1 where id={};".format(user_id,validTime,user_id))
				return HttpResponse(
					json.dumps({"code": 1, "msg": "未充值VIP！", "data": "user_id: {},会员时间：{}".format(user_id, validTime)}))
			user_id = is_true[0][0]
			timeArray = time.strptime(is_true[0][1], "%Y-%m-%d %H:%M:%S")
			timeStamp = int(time.mktime(timeArray))

			if timeStamp > int(time.time()):
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * month + timeStamp))
				sql.sql_exec("UPDATE biz_vip_record SET expire_time='{}' WHERE user_id= {};"
							 "update biz_user set is_vip=1 where id={};".format(validTime,user_id,user_id))
				return HttpResponse(json.dumps({"code": 1, "msg": "未过期！", "data": "{}".format(validTime)}))

			if timeStamp < int(time.time()):
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * month + int(time.time())))
				sql.sql_exec(
					"UPDATE biz_vip_record SET expire_time='{}' WHERE user_id= {};"
					"update biz_user set is_vip=1 where id={};".format(validTime, user_id, user_id))
				return HttpResponse(json.dumps({"code": 1, "msg": "过期！", "data": ""}))

		else:
			return HttpResponse(json.dumps({"code": 0, "msg": "请使用POST请求！", "data": ""}))
	except Exception as err:
		return HttpResponse(json.dumps({"code": 500, "msg": "addMembers 异常！", "data": "{}".format(err)}))


# def addMembers(request):
# 	if request.method == "POST":
# 		mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
# 		month = json.loads(request.body.decode().replace("'", "\"")).get('money')
# 		timeList = [0.5, 1, 3, 6]
#     else：
# 		# validityTime = 2592000 * month
#         # if len(mobile) != 11:
#         #     return HttpResponse(json.dumps({"code": 0, "msg": "手机号错误！", "data": ""}))
#         # if float(month) not in timeList:
#         #     return HttpResponse(json.dumps({"code": 0, "msg": "充值失败！充值月份不在范围", "data": ""}))
#         #
#         # if aa == []:
#         #     aaa = int(time.time()) + validityTime
#         #     print('未充值VIP')
#         #     return HttpResponse(json.dumps({"code": 1, "msg": "未充值VIP！", "data": ""}))
#         # timeArray = time.strptime(aa[0][0], "%Y-%m-%d %H:%M:%S")
#         # timeStamp = int(time.mktime(timeArray))
#         # print('ss', timeStamp)
#         # if timeStamp < int(time.time()):
#         #     return HttpResponse(json.dumps({"code": 1, "msg": "过期！", "data": ""}))
#         # if timeStamp > int(time.time()):
#         #     print("未过期")
#         #     return HttpResponse(json.dumps({"code": 1, "msg": "未过期！", "data": ""}))
#         # else:
# 		# tss1 = aa[0][0]
# 		# timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# 		# timeStamp = int(time.mktime(timeArray))
# 		# return HttpResponse(json.dumps({"code": 1, "msg": "充值成功！", "data": "{}".format(timeArray)}))


def removeUser(request):
	if request.method == "POST":
		print(request.body)
		mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
		is_mobile = sql.sql_select("SELECT status FROM biz_user WHERE mobile = '{}';".format(mobile))
		if is_mobile == []:
			return HttpResponse(json.dumps({"code": 0, "msg": "要删除的用户不存在！", "data": ""}))
		re = sql.sql_exec("exec RemoveUserByMobile '{}';".format(mobile))
		print("删除手机", mobile)
		return HttpResponse(json.dumps({"code": 1, "msg": "删除成功！", "data": "{}".format(re)}))
	else:
		return HttpResponse(json.dumps({"code": 0, "msg": "请使用POST请求！", "data": ""}))


import time


def testPortInsert(request):
	if request.method == "POST":
		try:
			mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
			money = json.loads(request.body.decode().replace("'", "\"")).get('money')
			print('mobile:', mobile)
			print('money:', money)
			sql = "INSERT INTO freight_id_payment (freight_id,id_s,`status`) VALUES ('DO-20200585685','{}',1)".format(
				time.time())
			mysqls.Data().query('localhost', sql)
			return HttpResponse(json.dumps({"code": 1, "msg": "请求成功！", "data": ""}))
		except Exception as err:
			return HttpResponse(json.dumps({"code": 0, "msg": "请求失败！", "data": "{}".format(err)}))
	else:
		return HttpResponse(json.dumps({"code": 0, "msg": "请使用POST请求！", "data": ""}))


def testPortSelect(request):
	if request.method == "POST":
		try:
			mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
			money = json.loads(request.body.decode().replace("'", "\"")).get('money')
			print('mobile:', mobile)
			print('money:', money)
			sql = "INSERT INTO freight_id_payment (freight_id,id_s,`status`) VALUES ('DO-20200585685','{}',1)".format(
				time.time())
			mysqls.Data().query('localhost', sql)
			return HttpResponse(json.dumps({"code": 1, "msg": "请求成功！", "data": ""}))
		except Exception as err:
			return HttpResponse(json.dumps({"code": 0, "msg": "请求失败！", "data": "{}".format(err)}))
	else:
		return HttpResponse(json.dumps({"code": 0, "msg": "请使用POST请求！", "data": ""}))


def testPort():
	pass

# testPortInsert()
