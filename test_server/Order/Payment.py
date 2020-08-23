from test_server import requestPort
import json
class Payment():
	def __init__(self):
		pass
	def	payment(self,freightId,payType):
		'''
		1(预付) 2（尾款）3（回单）
		:param freightId:
		:param payType:
		:return:
		'''
		data = {
		  "wlToken": "wl_token_1597895061527828",
		  "isCredit": "0",
		  "arrayPayment": json.dumps([
			{
			  "payType": payType,
			  "freightId": '{}'.format(freightId),
			  "payObjectNumber": 1,
			  "paymentAmount": 20,
			  "priceService": 1.23
			}
		  ])
		}
		url = '/api/invoice/pay'
		return requestPort.requestsPort(url,data)
# p = Payment()
# print(p.payment('DO-202008005696',1))

data = {
	'wlToken': 'wl_token_1598167999796727',
	'type': '',
	'payObjectSum': '1',
	'freightId': '{}',
	'payeeName': '黄华',
	'payeeMobile': '18007530000',
	'payeeId': '132521197806153017',
	'payeeBank': '农业银行',
	'payeeAccount': '6228481749128570570',
	'bankcardId': '1340',
	'isEntrust': '0',
	'finalPrice': '10.00'
}

a = {
  "wlToken": "wl_token_1598167999796727",
  "type": "1",
  "payObjectSum": "1",
  "freightId": "DO-202008006223",
  "payeeName": "黄华",
  "payeeMobile": "18007530115",
  "payeeId": "441481199907211134",
  "payeeBank": "交通银行",
  "payeeAccount": "6222620710028714937",
  "bankcardId": "1291",
  "isEntrust": "0",
  "advancePrice": "10.0"
}