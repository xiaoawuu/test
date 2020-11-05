# 初始化数据
from test_server.tmsPay.Modules.DriverInitialize import setDriverInitialize
from test_server.tmsPay.Modules.GetWlWallet import getWsBalance, getWlBalance, getUnpaidData, getDriverWallet, \
	gerInvoiceCompanyId
from test_server.utils.jsonRequestAPI import jsonAPI
from test_server.data.mysqls import Data
from test_server.tmsPay.Modules.TmsInitialize import insert
sql_ = Data().query

def WLinitialize(c_id):

	ws2_balance = getWsBalance(c_id)
	invoiceCompanyId = gerInvoiceCompanyId(c_id)
	invoice_company_balance = getWsBalance(invoiceCompanyId)
	print('插入',invoice_company_balance)
	ws_two_balance = getWlBalance(c_id)
	upaidData = getUnpaidData(c_id)
	print(upaidData["count_"])
	insert_ = insert(c_id,ws2_balance,ws_two_balance,upaidData["count_"],invoice_company_balance)
	print(insert_)
	return True

def EntrustInitialize(mobile):
	driverWallet = getDriverWallet(mobile)
	user_id = driverWallet['user_id']
	sum_balance = driverWallet['balance'] + driverWallet['out']
	balance = driverWallet['balance']
	freeze = driverWallet['freeze']
	extract = driverWallet['out']
	print(driverWallet)
	DriverInitialize = setDriverInitialize(user_id,mobile,balance,freeze,extract,sum_balance)
	print(DriverInitialize)

print(WLinitialize(764))
print(EntrustInitialize(13651770956))
