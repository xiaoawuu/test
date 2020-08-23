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
		data = {
		  "wlToken": dict_s['token'],
		  "type": dict_s['type'],
		  "payObjectSum": "1",
		  "freightId": "{}",
		  "payeeName": "贾献",
		  "payeeMobile": "16616666666",
		  "payeeId": "132521197806153017",
		  "payeeBank": "农业银行",
		  "payeeAccount": "6228481749128570570",
		  "bankcardId": "1340",
		  "isEntrust": "0",
		  "finalPrice": "20.0"
		}
		url = '/api/invoice/applyPayment'
		return requestPort.requestsPort(url,data)
a = applyForPayment()
dd = {'token':'','type':'1','freightId':'',}
print(a.applyForPaymentDriver(dd))

