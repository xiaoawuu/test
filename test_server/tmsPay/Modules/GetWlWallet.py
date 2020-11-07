from test_server.utils.jsonRequestAPI import jsonAPI
from test_server.data.mysqls import Data

sql_ = Data().query


def getWsBalance(c_id, type=2):
	'''
	获取网商钱包余额
	:param c_id:
	:param types:
	:return:
	'''
	if int(c_id) < 30 and type == 2:
		url = 'http://120.77.206.166:8200'
		path = '/pay/wsaccount/scbalqu'
		re_data = {
			"tmsId": str(c_id),
			"type": 4
		}
		try:
			response = jsonAPI(url, path, re_data)
			if response['code'] != 1:
				return '2.0网商余额查询异常'
			return response['data']
		except:
			return '2.0网商余额查询异常'
	elif int(c_id) < 30 and type == 1:
		url = 'http://120.77.206.166:8090'
		path = '/api/webbank/accountBalance'
		re_data = {"userid": "tms{}".format(c_id)}
		try:
			response = jsonAPI(url, path, re_data)
			if response['code'] != 1:
				return '1.0网商余额查询异常'
			elif response['data']['account_list'][0]['balance'] != response['data']['account_list'][0][
				'available_balance']:
				return '1.0网商余额查询异常'
			return response['data']['account_list'][0]['balance']
		except:
			return '1.0网商余额查询异常'

	status_sql = """
			SELECT ( CASE ws_two_status WHEN 2 THEN 1 ELSE 0 END ) ws_two_status,( CASE ws_status WHEN 2 THEN 1 ELSE 0 END ) ws_status
			FROM
				`tms_wl_wallet` 
			WHERE
				c_id = {};
		""".format(c_id)
	status = sql_('tms_test', status_sql)
	if status[0]['ws_two_status'] == 1 and status[0]['ws_status'] == 0:
		url = 'http://120.77.206.166:8200'
		path = '/pay/wsaccount/scbalqu'
		re_data = {
			"tmsId": str(c_id),
			"type": 4
		}
		try:
			response = jsonAPI(url, path, re_data)
			if response['code'] != 1:
				return '2.0网商余额查询异常'
			return response['data']
		except:
			return '2.0网商余额查询异常'

	elif status[0]['ws_two_status'] == 0 and status[0]['ws_status'] == 1:
		url = 'http://120.77.206.166:8090'
		path = '/api/webbank/accountBalance'
		re_data = {"userid": "tms{}".format(c_id)}
		try:
			response = jsonAPI(url, path, re_data)
			if response['code'] != 1:
				return '1.0网商余额查询异常'
			elif response['data']['account_list'][0]['balance'] != response['data']['account_list'][0][
				'available_balance']:
				return '1.0网商余额查询异常'
			return response['data']['account_list'][0]['balance']
		except:
			return '1.0网商余额查询异常'
	else:
		return '不支持除1.0和2.0外的公司'



def getWlBalance(c_id):
	'''
	获取物流钱包余额
	:param c_id:
	:param types:
	:return:
	'''
	status_sql = """
		SELECT ( CASE ws_two_status WHEN 2 THEN 1 ELSE 0 END ) ws_two_status,( CASE ws_status WHEN 2 THEN 1 ELSE 0 END ) ws_status
		FROM
			`tms_wl_wallet` 
		WHERE
			c_id = {};
	""".format(c_id)
	status = sql_('tms_test', status_sql)
	if status[0]['ws_two_status'] == 1 and status[0]['ws_status'] == 0:
		ws_two_balance = "SELECT ws_two_balance FROM tms_wl_wallet WHERE c_id = '{}';".format(c_id)
		ws_two_balance = sql_('tms_test', ws_two_balance)
		return ws_two_balance[0]["ws_two_balance"]

	elif status[0]['ws_two_status'] == 0 and status[0]['ws_status'] == 1:
		ws_two_balance = "SELECT ws_balance FROM tms_wl_wallet WHERE c_id = '{}';".format(c_id)
		ws_two_balance = sql_('tms_test', ws_two_balance)
		return ws_two_balance[0]["ws_balance"]
	else:
		return '不支持除1.0和2.0外的公司'


def getUnpaidData(c_id):
	'''
	获取待支付运单信息
	:param c_id:
	:return:
	'''
	unpaid = """
			SELECT
				COUNT(*) 'count_',
				SUM( pay_money ) 'pay_money',
				SUM( pay_service_money ) 'pay_service_money'
			FROM
				tms_wl_invoice_order A
				LEFT JOIN tms_wl_invoice_order_pay B ON A.freight_id = B.freight_id 
			WHERE
				A.c_id = {} 
			AND B.pay_status = 0;
		""".format(c_id)
	return sql_('tms_test', unpaid)[0]


def gerInvoiceCompanyId(c_id):
	sql = "SELECT invoice_company_id FROM tms_wl_logistics_company WHERE `id` = '{}';".format(c_id)
	invoice_company_id = sql_('tms_test', sql)
	return invoice_company_id[0]['invoice_company_id']


def getDriverWallet(mobile):
	a = """
			SELECT
			B.user_id, 
			B.balance,
			B.freeze,
			B.`out` 
		FROM
			zyb_customer A
			JOIN zyb_tms_wallet B ON A.id = B.user_id 
		WHERE
			mobile = '{}';
		""".format(mobile)
	wallet = sql_('zyb_test', a)
	money = {
		'user_id': wallet[0]["user_id"],
		'balance': wallet[0]["balance"],
		'freeze': wallet[0]["freeze"],
		'out': wallet[0]["out"]
	}
	return money

