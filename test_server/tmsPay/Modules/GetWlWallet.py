from test_server.tmsPay.Modules.TmsInitialize import getInvoiceCompanyType
from test_server.utils.jsonRequestAPI import jsonAPI
from test_server.data.mysqls import Data
from test_server.tmsPay.utils.responseJSON import responseJSON_0, responseJSON_1
from test_server.tmsPay.utils.print_ import *

sql_ = Data().query


def getWsBalance(c_id, a):
	'''
	获取网商钱包余额
	:param c_id:
	:param types:
	:return:
	'''
	if a == 2:
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
	elif a == 1:
		url = 'http://120.77.206.166:8090'
		path = '/api/webbank/accountBalance'
		re_data = {"userid": "tms{}".format(c_id)}
		try:
			response = jsonAPI(url, path, re_data)
			if response['code'] != 1:
				return '1.0网商余额查询异常1'
			elif response['data']['account_list'][0]['balance'] != response['data']['account_list'][0][
				'available_balance']:
				return responseJSON_0('1.0网商余额查询异常3', 'balance != available_balance')
			return response['data']['account_list'][0]['balance']
		except Exception as err:
			return responseJSON_0('1.0网商余额查询异常3', err)


'''
	status_sql = """
			SELECT ( CASE ws_two_status WHEN 2 THEN 1 ELSE 0 END ) ws_two_status,( CASE ws_status WHEN 2 THEN 1 ELSE 0 END ) ws_status
			FROM
				`tms_wl_wallet` 
			WHERE
				c_id = {};
		""".format(c_id)
	status = sql_('tms_test', status_sql)
	print_err(status)
	if invoiceCompanyType == 2:
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

	elif invoiceCompanyType == 1:
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

'''

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


def getZybdbWallet(mobile):
	'''
	获取司机/车队的钱包余额
	:param mobile:
	:return:
	'''
	user_type = "SELECT user_type FROM `zyb_customer` WHERE `account`='{}';".format(mobile)
	is_driver = '''SELECT
			COUNT(*) count_ 
		FROM
			zyb_driver_person_cert A
			JOIN zyb_customer B ON A.user_id = B.id 
		WHERE
			B.account = '{}';
	'''.format(mobile)
	user_type = sql_('zyb_test', user_type)
	if user_type[0]['user_type'] == 8:
		is_driver = sql_('zyb_test', is_driver)
		if is_driver[0]['count_'] > 0:
			re = responseJSON_0('请勿使用多角色的账户', mobile)
			return re
		wallet = """
				SELECT
					B.user_id, 
					B.balance,
					B.freeze,
					B.`out` 
			FROM
				zyb_customer A
				JOIN zyb_tms_wallet B ON A.id = B.user_id 
			WHERE
				A.mobile = '{}';
			""".format(mobile)
	elif user_type[0]['user_type'] == 2:

		wallet = """
		
				SELECT
					user_id,
					balance,
					freeze,
					`out` 
				FROM
					zyb_pay
					JOIN zyb_customer ON zyb_customer.id = zyb_pay.user_id 
				WHERE
					mobile = '{}';
				""".format(mobile)
	else:
		response = responseJSON_0('请输入车队或司机账户', mobile)
		return response
	wallet = sql_('zyb_test', wallet)
	if len(wallet) == 0:
		user_id = sql_('zyb_test', "SELECT id FROM zyb_customer WHERE mobile='{}';".format(mobile))
		wallet = [{'user_id': user_id[0]['id'], 'balance': '0', 'freeze': '0', 'out': '0'}]
	money = {
		'user_id': wallet[0]["user_id"],
		'balance': wallet[0]["balance"],
		'freeze': wallet[0]["freeze"],
		'out': wallet[0]["out"]
	}
	return responseJSON_1(data=money)
