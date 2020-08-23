from test_server import requestPort
import json
class sendOrders():
    '''
    :派单
    '''
    def __init__(self):
        pass
    def sendDriver(self,order,token,data):
        print('sendDriver')
        self.data = {
          "wlToken":'{}'.format(token),
          "orderId": '{}'.format(order),
          "type": "1",
          "sendOrder": json.dumps(data)
        }
        url = '/api/freight/addFreight'
        return requestPort.requestsPort(url,self.data)
# s = sendOrders()
datas = {
        "driverMobile": "16616666666",
        "driverName": "贾献",
        "driverNumber": "辽MQ7369",
        "subsistMoney": "10.00",
        "tailMoney": "20.00",
        "backMoney": "30.00",
        "oilMoney": "40.00",
        "etcMoney": "50.00",
        "isInvoice": 1,
        "isAgree": 1,
        "idCard": "132521197806153017",
        "totalMoney": "150.00"
    }
# print(s.sendDriver('LO-202008009307','wl_token_1597830470529726',datas))
