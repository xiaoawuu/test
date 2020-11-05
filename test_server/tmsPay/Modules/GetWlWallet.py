from test_server.utils.jsonRequestAPI import jsonAPI
from test_server.data.mysqls import Data

sql_ = Data().query


def getWsBalance(c_id, types=2):
	'''
	获取网商钱包余额
	:param c_id:
	:param types:
	:return:
	'''
	if types == 2:
		url = 'http://120.77.206.166:8200'
		path = '/pay/wsaccount/scbalqu'
		re_data = {
			"tmsId": str(c_id),
			"type": 4
		}
		try:
			response = jsonAPI(url, path, re_data)
			if response['code'] != 1:
				return False
			print('网商余额:',response['data'])
			return response['data']
		except:
			return False


print(getWsBalance(1))

def getWlBalance(c_id, types=2):
	'''
	获取物流钱包余额
	:param c_id:
	:param types:
	:return:
	'''
	if types == 2:
		ws_two_balance = "SELECT ws_two_balance FROM tms_wl_wallet WHERE c_id = '{}';".format(c_id)
		ws_two_balance = sql_('tms_test', ws_two_balance)
		return ws_two_balance[0]["ws_two_balance"]


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

print(gerInvoiceCompanyId(764))
# print(getUnpaidData(764)["count_"])
# print(getWlBalance(764))
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
		'user_id':wallet[0]["user_id"],
		'balance': wallet[0]["balance"],
		'freeze': wallet[0]["freeze"],
		'out': wallet[0]["out"]
	}
	return money



# print(getDriverWallet(13651770956))
