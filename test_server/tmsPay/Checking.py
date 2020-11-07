import time

from test_server.tmsPay.Initialize import WLinitialize, EntrustInitialize
from test_server.tmsPay.Modules.TmsInitialize import getPayOrderCount, getPayWallet
from test_server.tmsPay.Modules.DriverInitialize import grtDriverAddWaller




def checking(c_id_list,mobile_list):
	tms_pay_waller = 0.00
	tms_pay_waller = 0.00
	driver_add_waller = 0.00
	execute_time = int(time.time())
	for	c_id in c_id_list:
		WLinitialize(c_id,execute_time)
	for mobile in mobile_list:
		EntrustInitialize(mobile,execute_time)
	for c_id in c_id_list:
		PaWallet = getPayWallet(c_id)
		print(PaWallet)
		tms_pay_waller  += float(PaWallet)
	for mobile in mobile_list:
		driverAddWaller = grtDriverAddWaller(mobile)
		driver_add_waller += float(driverAddWaller)
	# payFreight = getPayOrderCount(c_id)
	print('TMS支出总额：',tms_pay_waller)
	print('司机收入总额：',driver_add_waller)

checking([764,],[13651770956])
