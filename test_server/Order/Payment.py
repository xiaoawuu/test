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