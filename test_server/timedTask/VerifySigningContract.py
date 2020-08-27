
from test_server.data.mysqls import Data
import datetime
from test_server.timedTask.utils.WriteLog import writeLog
class VerifySigningContract():
	def __init__(self):
		self.data = Data()
		self.yesterday = datetime.date.today() + datetime.timedelta(-1)
	def contractOfAffreightment(self):
		'''
		检验承运合同
		:return:
		'''
		try:
			sql = "SELECT * FROM (SELECT fre1.freight_id FROM	tms_wl_freight fre1 WHERE ( fre1.create_time BETWEEN" \
				  " '{} 00:00:00' AND '{} 23:59:59' ) AND fre1.`status` IN ( 12, 14, 15, 16, 17 ) AND freight_id" \
				  " != first_order_id) B WHERE (	SELECT count( 1 ) num FROM ( SELECT com1.freight_id FROM tms_commission_contract" \
				  " com1 WHERE com1.contract_type = 2 ) A WHERE A.freight_id = B.freight_id ) = 0 ;".format(self.yesterday,self.yesterday)
			isTrue = self.data.query('tms_live_r',sql)
			writeLog('未签署承运合同的运单',isTrue)
			return True
		except Exception:
			return False



