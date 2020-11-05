from test_server.utils.jsonRequestAPI import jsonAPI
from test_server.data.mysqls import Data


def getWsBalance(c_id,types=2):
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
			return response['data']
		except:
			return False

