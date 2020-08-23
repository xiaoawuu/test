'''
运单终结
'''
import json
from test_server import requestPort
class freightFinality():
	def	__init__(self):
		pass
	def tmsFinality(self,token,freight):
		data = {
		  "wlToken": token,
		  "type": "4",
		  "IsInvoice": "1",
		  "userType": "C",
		  "imgUrlStr": json.dumps({
			"img": []
		  }),
		  "freightId": freight
		}
		url = '/api/freight/finality'
		return requestPort.requestsPort(url,data)
# f = freightFinality()
# print(f.tmsFinality(1))
# {
#   "wlToken": "wl_token_1597628012966726",
#   "freightId": "DO-202008005580",
#   "type": "4",
#   "IsInvoice": "1",
#   "userType": "C",
#   "imgUrlStr": []
# }
