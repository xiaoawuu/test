from test_server.data.mysqls import Data
import datetime, time
from test_server.timedTask.utils.WriteLog import writeLog
import json


class VerifySigningContract():
	def __init__(self):
		self.data = Data()
		yesterday = datetime.date.today() + datetime.timedelta(-1)
		self.startTime = '{} 00:00:00'.format(yesterday)
		self.endTime = '{} 23:59:59'.format(yesterday)
		self.startTimestamp = int(time.mktime(time.strptime(self.startTime, "%Y-%m-%d %H:%M:%S")))
		self.endTimestamp = int(time.mktime(time.strptime(self.endTime, "%Y-%m-%d %H:%M:%S")))

	def contractOfAffreightment(self):
		'''
		检验承运合同
		:return:
		'''
		try:
			sql = "SELECT * FROM (SELECT fre1.freight_id FROM	tms_wl_freight fre1 WHERE ( fre1.create_time BETWEEN" \
				  " '{}' AND '{}' ) AND fre1.`status` IN ( 12, 14, 15, 16, 17 )) B WHERE (SELECT count(1) num FROM (SELECT com1.freight_id FROM tms_commission_contract" \
				  " com1 WHERE com1.contract_type = 2 ) A WHERE A.freight_id = B.freight_id ) = 0 ;".format(
				self.startTime, self.endTime)
			print("检验承运合同")
			isTrue = self.data.query('tms_live_r', sql)
			writeLog('未签署承运合同的运单', isTrue)
			return isTrue
		except Exception as err:
			writeLog('contractOfAffreightment>>>error:', err)
			return err

	def checkTheContract(self):
		'''
		检验托运合同
		:return:
		'''
		try:
			sql = "SELECT * FROM (SELECT fre1.first_order_id FROM tms_wl_freight fre1 " \
				  "WHERE (fre1.create_time BETWEEN '{}' AND '{}') " \
				  "AND fre1.`status` IN ( 12, 14, 15, 16, 17 )) B WHERE (SELECT count( 1 ) num FROM ( " \
				  "SELECT com1.order_id FROM tms_commission_contract com1 WHERE com1.contract_type = 3 ) " \
				  "A WHERE	A.order_id = B.first_order_id) = 0;".format(self.startTime, self.endTime, )
			isTrue = self.data.query('tms_live_r', sql)
			writeLog('未签署托运合同的订单', isTrue)
			print("检验托运合同")
			return isTrue
		except Exception as err:
			writeLog('checkTheContract>>>error:', err)
			return err

	def letterOfEntrustment(self):
		list_s = []
		'''
		委托函
		:return:
		'''
		try:
			signFreightIdSQL = "SELECT C.waybill_sn,D.phone,D.card_name FROM zyb_pay_order A JOIN zyb_tms_wallet_out B " \
							   "ON A.pay_out_id =  B.id JOIN zyb_tms_wallet_log C ON A.pay_log_id = C.id JOIN zyb_tms_wallet_bankcard " \
							   "D on B.bankcard_id = D.id WHERE add_time BETWEEN '{}' AND '{}'".format(
				self.startTimestamp, self.endTimestamp)
			responseData = self.data.query('zyb_live_r', signFreightIdSQL)
			print("检测委托函")
			for i in responseData:

				sql = "SELECT driver_name,driver_mobile FROM tms_wl_freight WHERE freight_id ='{}';".format(
					i['waybill_sn'])
				response = self.data.query('tms_live_r', sql)
				if i['phone'] != response[0]['driver_mobile']:
					comm_sql = "SELECT count(*) A FROM tms_commission_contract WHERE contract_type = 1 AND freight_id = '{}'".format(
						i['waybill_sn'])
					response_comm = self.data.query('tms_live_r', comm_sql)
					if response_comm[0]['A'] == 0:
						list_s.append(i['waybill_sn'])
			if len(list_s) > 1:
				writeLog('未签署w委托合同的运单', list_s)
		except Exception as err:
			writeLog('letterOfEntrustment>>>error:', err)


# v = VerifySigningContract()
# print(v.contractOfAffreightment())
# v.letterOfEntrustment()


'''
司机
SELECT * FROM zyb_pay_order RIGHT JOIN zyb_pay_log ON zyb_pay_order.pay_log_id = zyb_pay_log.id WHERE zyb_pay_order.type = 1 AND zyb_pay_order.add_time BETWEEN '1598544000' AND '1598630399';
车队
SELECT * FROM zyb_pay_order RIGHT JOIN zyb_tms_wallet_log ON zyb_pay_order.pay_log_id = zyb_tms_wallet_log.id WHERE zyb_pay_order.type = 2 AND zyb_pay_order.add_time BETWEEN '1598544000' AND '1598630399';


车队：三遍关联
SELECT * FROM `zyb_pay_order` JOIN zyb_tms_wallet_out ON zyb_pay_order.pay_out_id =  zyb_tms_wallet_out.id JOIN zyb_tms_wallet_log ON zyb_pay_order.pay_log_id = zyb_tms_wallet_log.id  WHERE add_time BETWEEN '1598544000' AND '1598630399' AND zyb_pay_order.type = 2;
司机：三遍关联
SELECT * FROM `zyb_pay_order` JOIN zyb_pay_out ON zyb_pay_order.pay_out_id =  zyb_pay_out.id JOIN zyb_pay_log ON zyb_pay_order.pay_log_id = zyb_pay_log.id  WHERE add_time BETWEEN '1598544000' AND '1598630399' AND zyb_pay_order.type = 1;

已申请付款的单子：
(SELECT zyb_tms_wallet_log.waybill_sn FROM `zyb_pay_order`  JOIN zyb_tms_wallet_log ON zyb_pay_order.pay_log_id = zyb_tms_wallet_log.id  WHERE zyb_pay_order.add_time BETWEEN '1598544000' AND '1598630399')
 UNION 
(SELECT waybill_sn FROM `zyb_pay_order` JOIN zyb_pay_log ON zyb_pay_order.pay_log_id = zyb_pay_log.id  WHERE add_time BETWEEN '1598544000' AND '1598630399' AND zyb_pay_order.type = 1);

SELECT C.waybill_sn,D.phone,D.card_name FROM zyb_pay_order A JOIN zyb_tms_wallet_out B ON A.pay_out_id =  B.id JOIN zyb_tms_wallet_log C ON A.pay_log_id = C.id JOIN zyb_tms_wallet_bankcard D on B.bankcard_id = D.id WHERE add_time BETWEEN '1598544000' AND '1598630399' AND A.type = 2;

'''
