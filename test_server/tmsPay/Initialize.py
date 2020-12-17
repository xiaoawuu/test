# 初始化数据
from test_server.tmsPay.Modules.DriverInitialize import setDriverInitialize
from test_server.tmsPay.Modules.GetWlWallet import getWsBalance, getWlBalance, getUnpaidData, getZybdbWallet, \
	gerInvoiceCompanyId
from test_server.tmsPay.Modules.TmsInitialize import delete as tms_delete, getInvoiceCompanyType
from test_server.tmsPay.Modules.DriverInitialize import delete as mobile_delete
from test_server.data.mysqls import Data
from test_server.tmsPay.Modules.TmsInitialize import insert
from test_server.tmsPay.utils.print_ import *
from test_server.tmsPay.utils.responseJSON import responseJSON_0,responseJSON_1
sql_ = Data().query
import time


#
def WLinitialize(c_id, execute_time):
	invoiceCompanyType = getInvoiceCompanyType(c_id)
	ws2_balance = getWsBalance(c_id,invoiceCompanyType["msg"])
	invoiceCompanyId = gerInvoiceCompanyId(c_id)
	invoice_company_balance = getWsBalance(invoiceCompanyId,invoiceCompanyType["msg"])
	ws_two_balance = getWlBalance(c_id)
	upaidData = getUnpaidData(c_id)
	insert_ = insert(c_id, ws2_balance, ws_two_balance, upaidData["count_"], invoice_company_balance, execute_time)
	if insert_['code'] == 0:
		return insert_
	return responseJSON_1('TMS初始化成功！',insert_)


def EntrustInitialize(mobile, execute_time):
	driverWallet = getZybdbWallet(mobile)
	if driverWallet['code'] == 0:
		return driverWallet
	user_id = driverWallet['data']['user_id']
	sum_balance = driverWallet['data']['balance'] + driverWallet['data']['out']
	balance = driverWallet['data']['balance']
	freeze = driverWallet['data']['freeze']
	extract = driverWallet['data']['out']
	DriverInitialize = setDriverInitialize(user_id, mobile, balance, freeze, extract, sum_balance, execute_time)
	if DriverInitialize['code'] == 0:
		return DriverInitialize
	return responseJSON_1('初始化成功')

def checking(c_id_list, mobile_list):
	execute_time = int(time.time())
	for i in mobile_list:
		mobile_delete(i)
	for i in c_id_list:
		tms_delete(i)
	for c_id in c_id_list:
		WLinitialize(c_id, execute_time)
	for mobile in mobile_list:
		is_true = EntrustInitialize(mobile, execute_time)
		if is_true['code'] == 0:
			return is_true
	return responseJSON_1('初始化成功！','初始化代码:{}'.format(execute_time))

if __name__ == '__main__':
	print_suc(checking([810,811],[16615599999,16616666666,18007555555]))

