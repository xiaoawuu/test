import datetime
from test_server.data.mysqls import Data


class GetOrderData():
	'''
	获取前一天的订单数据(status in (12,14,15,16,17) )
	:status = 1 是需要有合同的单子，其他相反
	'''

	def __init__(self):
		self.Data = Data()
		self.yesterday = datetime.date.today() + datetime.timedelta(-1)
		print('时间:', self.yesterday)

	def getFreightId(self, status=1):
		if status == 1:
			self.freight_data = self.Data.query('tms_test',
												"SELECT freight_id FROM tms_wl_freight WHERE (last_update_time BETWEEN '{} 00:00:00'"
												" AND '{} 23:59:59') AND `status` in (12,14,15,16,17);".format(
													self.yesterday, self.yesterday))
		else:
			self.freight_data = self.Data.query('tms_test',
												"SELECT freight_id FROM tms_wl_freight WHERE (last_update_time BETWEEN '{} 00:00:00'"
												" AND '{} 23:59:59') AND `status` in (11,13);".format(
													self.yesterday, self.yesterday))
		return self.freight_data

	def getOrderId(self, status=1):
		if status == 1:

			self.order_data = self.Data.query('tms_test',
											  "SELECT first_order_id FROM tms_wl_freight WHERE (last_update_time BETWEEN '{} 00:00:00'"
											  " AND '{} 23:59:59') AND `status` in (12,14,15,16,17);".format(
												  self.yesterday,
												  self.yesterday))
		else:
			self.order_data = self.Data.query('tms_test',
											  "SELECT first_order_id FROM tms_wl_freight WHERE (last_update_time BETWEEN '{} 00:00:00'"
											  " AND '{} 23:59:59') AND `status` in (11,13);".format(
												  self.yesterday,
												  self.yesterday))
		return self.order_data


# d = GetOrderData()
# d.getFreightId()
# d.getOrderId()
sql = "SELECT	* FROM (SELECT fre1.freight_id FROM	tms_wl_freight fre1 WHERE ( fre1.last_update_time BETWEEN '2020-08-25 00:00:00' AND '2020-08-25 23:59:59' ) AND fre1.`status` IN ( 12, 14, 15, 16, 17 ) AND freight_id != first_order_id) B WHERE (	SELECT count( 1 ) num FROM ( SELECT com1.freight_id FROM tms_commission_contract com1 WHERE com1.contract_type = 2 ) A WHERE A.freight_id = B.freight_id ) = 0 ;"
