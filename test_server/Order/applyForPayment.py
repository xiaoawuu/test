from test_server import requestPort

class applyForPayment():
	def __init__(self):
		pass
	def applyForPaymentDriver(self,dict_s):
		'''
		:request:申请付款
		:param dict_s:{}
		:return:
		:payObjectSum:1是司机,2是车队
		'''
		# table_s = {
		#   "wlToken": dict_s['token'],
		#   "type": dict_s['type'],
		#   "payObjectSum": "1",
		#   "freightId": "{}",
		#   "payeeName": "贾献",
		#   "payeeMobile": "16616666666",
		#   "payeeId": "132521197806153017",
		#   "payeeBank": "农业银行",
		#   "payeeAccount": "6228481749128570570",
		#   "bankcardId": "1340",
		#   "isEntrust": "0",
		#   "finalPrice": "20.0"
		# }
		url = '/api/invoice/applyPayment'
		return requestPort.requestsPort(url,dict_s)
# aa = {	'wlToken': 'wl_token_1598167999796727',
# 	'type': '1',
# 	'payObjectSum': '1',
# 	'freightId': 'DO-202008006242',
# 	'payeeName': '黄华',
# 	'payeeMobile': '18007530000',
# 	'payeeId': '132521197806153017',
# 	'payeeBank': '农业银行',
# 	'payeeAccount': '6228481749128570570',
# 	'bankcardId': '1340',
# 	'isEntrust': '0',
# 	'advancePrice': '10.00'
# }
# a = applyForPayment()
# dd = {'token':'','type':'1','freightId':'',}
# print(a.applyForPaymentDriver(aa))
#

import requests
import json


def test_a(id):
	url = "http://120.76.242.220:9099/account/qryPersonAcctByAcctId"

	payload = json.dumps({
	  "accountId": "{}".format(id),
	  "email": "string",
	  "mobile": "",
	  "name": ""
	})
	headers = {
	  'Content-Type': 'application/json'
	}

	response = requests.request("POST", url, headers=headers, data=payload)
	print(response.text)
