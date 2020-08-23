import requests
import json
from test_server import requestPort



class Order():
    def __init__(self):
        pass
    def addOrder(self,data,token):
        self.data = data
        self.token = token
        re_data = {
            'wlToken':'{}'.format(self.token),
            'tmsWLOrder':json.dumps(self.data)
        }
        url = "/api/order/addOrder"
        print('派单')
        return requestPort.requestsPort(url,re_data)


# o = Order()
# print(o.addOrder(2))
