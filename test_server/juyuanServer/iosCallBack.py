from test_server.data.sql import sql_select

class CallBack():
	def __init__(self):
		self.diteData = {}
		pass
	def iosCallBack(self):
		try:
			data =  sql_select('SELECT order_sn,receipt FROM apple_pay_callback_log WHERE status != 0 ;')
			for i in data:
				self.diteData[i[1]] = i[0]
				print(self.diteData[i[1]])

			print(self.diteData)
			print(len(self.diteData))
		except Exception as a:
			return a

c = CallBack()

c.iosCallBack()
