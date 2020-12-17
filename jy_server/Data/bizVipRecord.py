from jy_server.Data.sysLog import insert
from test_server.utils.responseJSON import responseJSON_1, responseJSON_0
from test_server.data.sql import sql_select, sql_exec


def getBizVipRecord(parameter):
	if len(parameter) == 11:
		sql = '''
			SELECT
				B.expire_time 
			FROM
				biz_user A
				JOIN biz_vip_record B ON A.id = B.user_id 
			WHERE
				sex = 1 
				AND A.mobile= '{}';
		'''.format(parameter)
	else:
		sql = "SELECT expire_time FROM biz_vip_record WHERE user_id = {};".format(parameter)
	sql = sql_select(sql)
	if len(sql) < 1:
		return responseJSON_0('未开通会员')
	return responseJSON_1(sql[0][0])


def setBizVipRecord(user_id, expire_time,money):
	print('时间',user_id,expire_time)
	try:
		sql = "SELECT * FROM biz_vip_record WHERE user_id = '{}';".format(user_id)
		sql = sql_select(sql)
		if sql == []:
			sql = '''
				INSERT INTO biz_vip_record (user_id,expire_time) VALUES ({},'{}');
				update biz_user set is_vip=1 where id={};
				'''.format(user_id, expire_time, user_id)
			sql_exec(sql)
			insert(user_id,'setBizVipRecord','TEST:充值{}个月会员'.format(money))
			return responseJSON_1('充值成功！', '会员时间：{}'.format(expire_time))
		sql = '''
			UPDATE biz_vip_record SET expire_time='{}' WHERE user_id= {};
			UPDATE biz_user set is_vip=1 where id={};
		'''.format(expire_time, user_id, user_id)
		sql_exec(sql)
		insert(user_id, 'setBizVipRecord', 'TEST:充值{}个月会员'.format(money))
		return responseJSON_1('充值成功！', '会员时间：{}'.format(expire_time))

	except Exception as error:
		return responseJSON_0('setBizVipRecord方法异常', error)