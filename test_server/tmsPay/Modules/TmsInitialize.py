import time
from test_server.tmsPay.utils.responseJSON import responseJSON_0,responseJSON_1
from test_server.data.mysqls import Data
from test_server.tmsPay.utils.print_ import *

sql_ = Data().query
path = r'C:\test_server\test\test_server\tmsPay\Initialize.py'

def getInvoiceCompanyType(c_id):
	type = '''
		SELECT ws_status,ws_two_status FROM tms_wl_wallet WHERE `c_id` = '{}';
	'''.format(c_id)
	type = sql_('tms_test',type)
	if len(type) < 1:
		return responseJSON_1(0)
	ws_status = type[0]['ws_status']
	ws_two_status = type[0]['ws_two_status']
	if ws_status == 2 and (ws_two_status == 0 or ws_two_status):
		return responseJSON_1(1)
	elif ws_two_status == 2 and (ws_status == 0 or ws_status == 4):
		return responseJSON_1(2)
	else:
		print_err('请使用网商1.0或网商2.0物流公司' + 'c_id:{}'.format(c_id))
		return responseJSON_0(0)


# print_warn_(getInvoiceCompanyType(770))

def insert(c_id, ws_wallet, wl_wallet, pay_order_count, invoice_wallet, execute_time):
	try:
		sql = """
			INSERT INTO tms_initialize ( c_id, ws_wallet, wl_wallet, pay_order_count,invoice_wallet,time ) VALUES ( %s, %s, %s, %s ,%s, %s);
			""" % (
			c_id, str(ws_wallet), str(wl_wallet), int(pay_order_count), str(invoice_wallet), str(execute_time))
		data = sql_('localhost', sql)
		print_suc(sql)
		if len(data) == 0:
			print_warn_('数据更新成功！')
			return responseJSON_1('数据')
		else:print_err(data)
	except TypeError as err:
		return responseJSON_0('数据',err)


def delete(c_id, ):
	try:
		sql = "DELETE FROM `tms_initialize` WHERE c_id={};".format(c_id)
		sql_('localhost', sql)
		return responseJSON_1('删除成功')
	except TypeError as err:
		return responseJSON_0('删除成功',err )


def getPayOrderCount(c_id):
	'''
	获取支付单子的数量
	:param c_id:
	:return:
	'''
	sql = """SELECT pay_order_count - (SELECT pay_order_count FROM tms_initialize WHERE c_id = '{}' ORDER BY id DESC LIMIT 0,1
		) `count_` FROM tms_initialize WHERE c_id = '{}' ORDER BY id DESC LIMIT 1,1;""".format(c_id, c_id)
	re = sql_('localhost', sql)
	return re[0]['count_']


def getPayWallet(c_id):
	'''
	获取支付的金额
	:param c_id:
	:return:
	'''
	sql = """SELECT ws_wallet - (SELECT ws_wallet FROM tms_initialize WHERE c_id = '{}' ORDER BY id DESC LIMIT 0,1
		) `ws_wallet` FROM tms_initialize WHERE c_id = '{}' ORDER BY id DESC LIMIT 1,1;""".format(c_id, c_id)
	re = sql_('localhost', sql)
	return re[0]['ws_wallet']


def getServiceFeeIncomet(c_id, ):
	'''
	获取收入的服务费
	:param c_id:
	:return:
	'''
	sql = """SELECT invoice_wallet - (SELECT invoice_wallet FROM tms_initialize WHERE c_id = '{}' ORDER BY id DESC LIMIT 1,1
		) `invoice_wallet` FROM tms_initialize WHERE c_id = '{}' ORDER BY id DESC LIMIT 0,1;""".format(c_id, c_id)
	re = sql_('localhost', sql)
	return re[0]['invoice_wallet']
