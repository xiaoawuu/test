import time

from test_server.tmsPay.Initialize import WLinitialize,EntrustInitialize
from test_server.tmsPay.Modules.GetWlWallet import gerInvoiceCompanyId
from test_server.tmsPay.Modules.TmsInitialize import getPayOrderCount, getPayWallet, getServiceFeeIncomet
from test_server.tmsPay.Modules.DriverInitialize import grtDriverAddWaller




def checking(c_id_list,mobile_list):
	service_charge_add = 0.00
	tms_pay_waller = 0.00
	driver_add_waller = 0.00
	execute_time = int(time.time())
	for	c_id in c_id_list:
		WLinitialize(c_id,execute_time)
	for mobile in mobile_list:
		EntrustInitialize(mobile,execute_time)
	for c_id in c_id_list:
		PayWallet = getPayWallet(c_id)
		ServiceFeeIncomet = getServiceFeeIncomet(c_id)
		tms_pay_waller  += float(PayWallet)
		service_charge_add  += float(ServiceFeeIncomet)

	for mobile in mobile_list:
		driverAddWaller = grtDriverAddWaller(mobile)
		driver_add_waller += float(driverAddWaller)

	print('TMS支出总额：',round(tms_pay_waller,3))
	print('司机收入总额：',driver_add_waller)
	print('服务费收入：',round(service_charge_add,3))
	print('服务费+司机收入：',round(service_charge_add+driver_add_waller,3))

checking([770,],[17864395278])
