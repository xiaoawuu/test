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
		setMealList = [0.5, 1, 3, 6]
		if float(money) in setMealList:
			money = float(money)
			is_mobile = sql.sql_select("SELECT status FROM biz_user WHERE mobile = '{}';".format(mobile))
			if is_mobile == []:
				return HttpResponse(json.dumps({"code": 0, "msg": "用户不存在！", "table_s": ""}))
			if is_mobile[0][0] != 4:
				return HttpResponse(json.dumps({"code": 0, "msg": "用户还未完成认证！", "table_s": ""}))
			if float(money) not in [0.5, 1, 3, 6]:
				return HttpResponse(json.dumps({"code": 0, "msg": "充值失败,充值月份不在范围！", "table_s": ""}))
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
					json.dumps({"code": 1, "msg": "未充值VIP！", "table_s": "user_id: {},会员时间：{}".format(user_id, validTime)}))
			user_id = is_true[0][0]
			timeArray = time.strptime(is_true[0][1], "%Y-%m-%d %H:%M:%S")
			timeStamp = int(time.mktime(timeArray))

			if timeStamp > int(time.time()):
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * money + timeStamp))
				sql.sql_exec("UPDATE biz_vip_record SET expire_time='{}' WHERE user_id= {};"
							 "update biz_user set is_vip=1 where id={};".format(validTime, user_id, user_id))
				return HttpResponse(json.dumps({"code": 1, "msg": "未过期！", "table_s": "{}".format(validTime)}))

			if timeStamp < int(time.time()):
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * money + int(time.time())))
				sql.sql_exec(
					"UPDATE biz_vip_record SET expire_time='{}' WHERE user_id= {};"
					"update biz_user set is_vip=1 where id={};".format(validTime, user_id, user_id))
				return HttpResponse(json.dumps({"code": 1, "msg": "过期！", "table_s": ""}))

		else:
			if money == "" or mobile == "":
				return HttpResponse(json.dumps({"code": 0, "msg": "金额或金额类型异常", "table_s": ""}))
			if type(money) != int:
				money = int(money)
			if is_int.is_number(money) or type(money) != int:
				return HttpResponse(json.dumps({"code": 0, "msg": "金额或金额类型异常", "table_s": ""}))
			if money > 4000 or money < 1:
				return HttpResponse(json.dumps({"code": 0, "msg": "金额充值范围1~4000币", "table_s": ""}))
			is_mobile = sql.sql_select("SELECT status FROM biz_user WHERE mobile = '{}';".format(mobile))
			if is_mobile == []:
				return HttpResponse(json.dumps({"code": 0, "msg": "用户不存在！", "table_s": ""}))
			if is_mobile[0][0] != 4:
				return HttpResponse(json.dumps({"code": 0, "msg": "用户还未完成认证！", "table_s": ""}))

			return HttpResponse(json.dumps({"code": 1, "msg": "充值成功！", "table_s": "当前账户余额:{}"}))
	else:
		return HttpResponse(json.dumps({"code": 0, "msg": "请使用POST请求！", "table_s": ""}))


def addMembers(request):
	try:
		if request.method == "POST":
			mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
			month = json.loads(request.body.decode().replace("'", "\"")).get('month')
			if month == "" or mobile == "":
				return HttpResponse(json.dumps({"code": 0, "msg": "金额或金额类型异常", "table_s": ""}))
			is_mobile = sql.sql_select("SELECT status FROM biz_user WHERE mobile = '{}';".format(mobile))
			if is_mobile == []:
				return HttpResponse(json.dumps({"code": 0, "msg": "用户不存在！", "table_s": ""}))
			if is_mobile[0][0] != 4:
				return HttpResponse(json.dumps({"code": 0, "msg": "用户还未完成认证！", "table_s": ""}))
			if float(month) not in [0.5, 1, 3, 6]:
				return HttpResponse(json.dumps({"code": 0, "msg": "充值失败,充值月份不在范围！", "table_s": ""}))
			is_true = sql.sql_select(
				"SELECT A.id,B.expire_time FROM biz_user A JOIN biz_vip_record B ON A.id = B.user_id WHERE sex=1 AND A.mobile='{}';".format(
					mobile))
			if is_true == []:
				user_id = sql.sql_select("SELECT id FROM biz_user WHERE mobile = '{}';".format(mobile))[0][0]
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * month + int(time.time())))
				sql.sql_exec(
					"INSERT INTO biz_vip_record (user_id,expire_time) VALUES ({},'{}');"
					"update biz_user set is_vip=1 where id={};".format(user_id, validTime, user_id))
				return HttpResponse(
					json.dumps({"code": 1, "msg": "未充值VIP！", "table_s": "user_id: {},会员时间：{}".format(user_id, validTime)}))
			user_id = is_true[0][0]
			timeArray = time.strptime(is_true[0][1], "%Y-%m-%d %H:%M:%S")
			timeStamp = int(time.mktime(timeArray))

			if timeStamp > int(time.time()):
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * month + timeStamp))
				sql.sql_exec("UPDATE biz_vip_record SET expire_time='{}' WHERE user_id= {};"
							 "update biz_user set is_vip=1 where id={};".format(validTime, user_id, user_id))
				return HttpResponse(json.dumps({"code": 1, "msg": "未过期！", "table_s": "{}".format(validTime)}))

			if timeStamp < int(time.time()):
				validTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(2678400 * month + int(time.time())))
				sql.sql_exec(
					"UPDATE biz_vip_record SET expire_time='{}' WHERE user_id= {};"
					"update biz_user set is_vip=1 where id={};".format(validTime, user_id, user_id))
				return HttpResponse(json.dumps({"code": 1, "msg": "过期！", "table_s": ""}))

		else:
			return HttpResponse(json.dumps({"code": 0, "msg": "请使用POST请求！", "table_s": ""}))
	except Exception as err:
		return HttpResponse(json.dumps({"code": 500, "msg": "addMembers 异常！", "table_s": "{}".format(err)}))


# def addMembers(request):
# 	if request.method == "POST":
# 		mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
# 		month = json.loads(request.body.decode().replace("'", "\"")).get('money')
# 		timeList = [0.5, 1, 3, 6]
#     else：
# 		# validityTime = 2592000 * month
#         # if len(mobile) != 11:
#         #     return HttpResponse(json.dumps({"code": 0, "msg": "手机号错误！", "table_s": ""}))
#         # if float(month) not in timeList:
#         #     return HttpResponse(json.dumps({"code": 0, "msg": "充值失败！充值月份不在范围", "table_s": ""}))
#         #
#         # if aa == []:
#         #     aaa = int(time.time()) + validityTime
#         #     print('未充值VIP')
#         #     return HttpResponse(json.dumps({"code": 1, "msg": "未充值VIP！", "table_s": ""}))
#         # timeArray = time.strptime(aa[0][0], "%Y-%m-%d %H:%M:%S")
#         # timeStamp = int(time.mktime(timeArray))
#         # print('ss', timeStamp)
#         # if timeStamp < int(time.time()):
#         #     return HttpResponse(json.dumps({"code": 1, "msg": "过期！", "table_s": ""}))
#         # if timeStamp > int(time.time()):
#         #     print("未过期")
#         #     return HttpResponse(json.dumps({"code": 1, "msg": "未过期！", "table_s": ""}))
#         # else:
# 		# tss1 = aa[0][0]
# 		# timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# 		# timeStamp = int(time.mktime(timeArray))
# 		# return HttpResponse(json.dumps({"code": 1, "msg": "充值成功！", "table_s": "{}".format(timeArray)}))


# Create your views here.
# -*- coding: utf-8 -*-

import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# django默认开启csrf防护，这里使用@csrf_exempt去掉防护
@csrf_exempt
def weixin_main(request):
	if request.method == "GET":
		# 接收微信服务器get请求发过来的参数
		signature = request.GET.get('signature', None)
		timestamp = request.GET.get('timestamp', None)
		nonce = request.GET.get('nonce', None)
		echostr = request.GET.get('echostr', None)
		# 服务器配置中的token
		token = '写你的token在这里'
		# 把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
		hashlist = [token, timestamp, nonce]
		hashlist.sort()
		hashstr = ''.join([s for s in hashlist])
		hashstr = hashlib.sha1(hashstr).hexdigest()
		if hashstr == signature:
			return HttpResponse(echostr)
		else:
			return HttpResponse("field")
	else:
		othercontent = autoreply(request)
		return HttpResponse(othercontent)


# 微信服务器推送消息是xml的，根据利用ElementTree来解析出的不同xml内容返回不同的回复信息，就实现了基本的自动回复功能了，也可以按照需求用其他的XML解析方法
import xml.etree.ElementTree as ET


def autoreply(request):
	try:
		webData = request.body
		xmlData = ET.fromstring(webData)

		msg_type = xmlData.find('MsgType').text
		ToUserName = xmlData.find('ToUserName').text
		FromUserName = xmlData.find('FromUserName').text
		CreateTime = xmlData.find('CreateTime').text
		MsgType = xmlData.find('MsgType').text
		MsgId = xmlData.find('MsgId').text

		toUser = FromUserName
		fromUser = ToUserName

		if msg_type == 'text':
			content = "您好,欢迎来到Python大学习!希望我们可以一起进步!"
			replyMsg = TextMsg(toUser, fromUser, content)
			print("成功了!!!!!!!!!!!!!!!!!!!")
			print(replyMsg)

			return replyMsg.send()

		elif msg_type == 'image':
			content = "图片已收到,谢谢"
			replyMsg = TextMsg(toUser, fromUser, content)
			return replyMsg.send()
		elif msg_type == 'voice':
			content = "语音已收到,谢谢"
			replyMsg = TextMsg(toUser, fromUser, content)
			return replyMsg.send()
		elif msg_type == 'video':
			content = "视频已收到,谢谢"
			replyMsg = TextMsg(toUser, fromUser, content)
			return replyMsg.send()
		elif msg_type == 'shortvideo':
			content = "小视频已收到,谢谢"
			replyMsg = TextMsg(toUser, fromUser, content)
			return replyMsg.send()
		elif msg_type == 'location':
			content = "位置已收到,谢谢"
			replyMsg = TextMsg(toUser, fromUser, content)
			return replyMsg.send()
		else:
			msg_type == 'link'
			content = "链接已收到,谢谢"
			replyMsg = TextMsg(toUser, fromUser, content)
			return replyMsg.send()

	except Exception as Argment:
		return Argment


class Msg(object):
	def __init__(self, xmlData):
		self.ToUserName = xmlData.find('ToUserName').text
		self.FromUserName = xmlData.find('FromUserName').text
		self.CreateTime = xmlData.find('CreateTime').text
		self.MsgType = xmlData.find('MsgType').text
		self.MsgId = xmlData.find('MsgId').text


import time


class TextMsg(Msg):
	def __init__(self, toUserName, fromUserName, content):
		self.__dict = dict()
		self.__dict['ToUserName'] = toUserName
		self.__dict['FromUserName'] = fromUserName
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['Content'] = content

	def send(self):
		XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
		return XmlForm.format(**self.__dict)




def removeUser(request):
	if request.method == "POST":
		print(request.body)
		mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
		is_mobile = sql.sql_select("SELECT status FROM biz_user WHERE mobile = '{}';".format(mobile))
		if is_mobile == []:
			return HttpResponse(json.dumps({"code": 0, "msg": "要删除的用户不存在！", "table_s": ""}))
		re = sql.sql_exec("exec RemoveUserByMobile '{}';".format(mobile))
		print("删除手机", mobile)
		return HttpResponse(json.dumps({"code": 1, "msg": "删除成功！", "table_s": "{}".format(re)}))
	else:
		return HttpResponse(json.dumps({"code": 0, "msg": "请使用POST请求！", "table_s": ""}))


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
			return HttpResponse(json.dumps({"code": 1, "msg": "请求成功！", "table_s": ""}))
		except Exception as err:
			return HttpResponse(json.dumps({"code": 0, "msg": "请求失败！", "table_s": "{}".format(err)}))
	else:
		return HttpResponse(json.dumps({"code": 0, "msg": "请使用POST请求！", "table_s": ""}))


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
			return HttpResponse(json.dumps({"code": 1, "msg": "请求成功！", "table_s": ""}))
		except Exception as err:
			return HttpResponse(json.dumps({"code": 0, "msg": "请求失败！", "table_s": "{}".format(err)}))
	else:
		return HttpResponse(json.dumps({"code": 0, "msg": "请使用POST请求！", "table_s": ""}))
