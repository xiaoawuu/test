import time

from test_server.data.sql import sql_select
from test_server.utils.responseJSON import responseJSON_1, responseJSON_0, responseJSON


def userStatus(mobile):
	'''
	用户是否认证
	:param mobile:
	:return:
	'''
	try:
		user_status = sql_select("SELECT status FROM biz_user WHERE mobile = '{}';".format(mobile))
		if user_status == []:
			return responseJSON_0('用户不存在！', mobile)
		if user_status[0][0] == 4:
			return responseJSON_1('已认证！', mobile)
		else:
			return responseJSON_0('未认证！', mobile)
	except Exception as error:
		return responseJSON_0('userStatus接口异常', error)


def vipStatus(mobile):
	'''
	会员状态
	:param mobile:
	:return:
	'''
	sql = '''
		SELECT
			A.id,
			B.expire_time 
		FROM
			biz_user A
			JOIN biz_vip_record B ON A.id = B.user_id 
		WHERE
			sex = 1 
			AND A.mobile= '{}';
	'''.format(mobile)
	try:
		vip_status = sql_select(sql)
		if vip_status == []:
			return responseJSON(code=1, msg='未开通')
		timeArray = time.strptime(vip_status[0][1], "%Y-%m-%d %H:%M:%S")
		timeStamp = int(time.mktime(timeArray))
		if timeStamp > int(time.time()):
			return responseJSON(code=2, msg='已开通', data=vip_status[0])
		return responseJSON(code=3, msg='已过期', data=vip_status[0])
	except Exception as error:
		return responseJSON_0('vipStatus接口异常', error)

