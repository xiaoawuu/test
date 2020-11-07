import time

from test_server.data.mysqls import Data
sql_ = Data().query
path = r'C:\test_server\test\test_server\tmsPay\Initialize.py'



def insert(c_id, ws_wallet, wl_wallet, pay_order_count, invoice_wallet, execute_time):
	try:
		sql = """
			INSERT INTO tms_initialize ( c_id, ws_wallet, wl_wallet, pay_order_count,invoice_wallet,time ) VALUES ( %s, %s, %s, %s ,%s, %s);
			""" % (
			c_id, str(ws_wallet), str(wl_wallet), int(pay_order_count), str(invoice_wallet), str(execute_time))
		data = sql_('localhost', sql)
		return data
	except TypeError as err:
		return err


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


def getServiceFeeIncomet(c_id,):
	'''
	获取收入的服务费
	:param c_id:
	:return:
	'''
	sql = """SELECT invoice_wallet - (SELECT invoice_wallet FROM tms_initialize WHERE c_id = '{}' ORDER BY id DESC LIMIT 1,1
		) `invoice_wallet` FROM tms_initialize WHERE c_id = '{}' ORDER BY id DESC LIMIT 0,1;""".format(c_id, c_id)
	re = sql_('localhost', sql)
	return re[0]['invoice_wallet']

