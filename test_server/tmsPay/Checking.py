from test_server.tmsPay.Initialize import WLinitialize, EntrustInitialize
from test_server.tmsPay.Modules.DriverInitialize import grtDriverAddWaller
from test_server.tmsPay.Modules.TmsInitialize import getPayWallet, getServiceFeeIncomet
from test_server.tmsPay.utils.responseJSON import responseJSON_1, responseJSON_0

from test_server.data.mysqls import Data
from test_server.tmsPay.utils.print_ import *

sql_ = Data().query


def checking(time):
	count_c_id = '''
		SELECT numbers count_c_id from (SELECT COUNT(c_id) as numbers FROM tms_initialize 
		WHERE time = '{}' GROUP BY c_id) a GROUP BY numbers;
	'''.format(time)
	count_mobile = '''
			SELECT numbers count_c_id from (SELECT COUNT(mobile) as numbers FROM driver_initialize 
			WHERE time = '{}' GROUP BY mobile) a GROUP BY numbers;
		'''.format(time)
	c_id = '''
	SELECT c_id FROM tms_initialize WHERE time = '{}' GROUP BY c_id;
	'''.format(time)
	mobile = '''
		SELECT mobile FROM driver_initialize WHERE time = '{}' GROUP BY mobile;
		'''.format(time)
	count_c_id = sql_('localhost', count_c_id)
	c_id = sql_('localhost', c_id)
	count_mobile = sql_('localhost', count_mobile)
	mobile = sql_('localhost', mobile)
	if len(count_c_id) == 0 or len(count_mobile) == 0:
		return responseJSON_0('初始化ID无效！', '初始化ID:{}'.format(time))
	elif len(count_c_id) == len(count_mobile) == 1:
		payTotalWallet = 0
		serviceFeeIncometTotal = 0
		driverAddWallerTotal = 0
		if count_c_id[0]['count_c_id'] == 1:
			'''
			未对账
			'''
			for i in c_id:
				initialize = WLinitialize(i['c_id'], time)
				if initialize['code'] == 0:
					return initialize
				print_warn_(initialize)
			for i in mobile:
				entrustInitialize = EntrustInitialize(i['mobile'], time)
				if entrustInitialize['code'] == 0:
					return initialize

			for i in c_id:
				payWallet = getPayWallet(i['c_id'])
				payTotalWallet += float(payWallet)
				print_suc(str(i['c_id']) + '物流公司支付:' + str(payWallet) + '元')

				serviceFeeIncomet = getServiceFeeIncomet(i['c_id'])
				print_suc(str(i['c_id']) + '物流公司分公司收入服务费:' + str(serviceFeeIncomet) + '元')
				serviceFeeIncometTotal += float(serviceFeeIncomet)

			for i in mobile:
				driverAddWaller = grtDriverAddWaller(i['mobile'])
				print_suc(str(i['mobile']) + '司机收入运费:' + str(driverAddWaller) + '元')
				driverAddWallerTotal += float(driverAddWaller)
			print_suc('\n物流公司总支出运费:{}'.format(payTotalWallet))
			print_suc('分公司总收入服务费:{}'.format(serviceFeeIncometTotal))
			print_suc('司机总收入运费:{}'.format(driverAddWallerTotal))
			if (payTotalWallet - serviceFeeIncometTotal) == driverAddWallerTotal:
				return responseJSON_1('\n---------------对账成功------------------！\n')
			else:
				return responseJSON_0('\n---------------对账失败！\n---------------')
		elif count_c_id[0]['count_c_id'] == 2:
			'''
			已对账
			'''

			for i in c_id:
				payWallet = getPayWallet(i['c_id'])
				print_suc(str(i['c_id']) + '物流公司支付:' + str(payWallet) + '元')
				payTotalWallet += float(payWallet)

				serviceFeeIncomet = getServiceFeeIncomet(i['c_id'])
				print_suc(str(i['c_id']) + '物流公司分公司收入服务费:' + str(serviceFeeIncomet) + '元')
				serviceFeeIncometTotal += float(serviceFeeIncomet)

			for i in mobile:
				driverAddWaller = grtDriverAddWaller(i['mobile'])
				print_suc(str(i['mobile']) + '司机收入运费:' + str(driverAddWaller) + '元')
				driverAddWallerTotal += float(driverAddWaller)
			print_suc('\n物流公司总支出运费:{}'.format(payTotalWallet))
			print_suc('分公司总收入服务费:{}'.format(serviceFeeIncometTotal))
			print_suc('司机总收入运费:{}'.format(driverAddWallerTotal))
			if (payTotalWallet - serviceFeeIncometTotal) == driverAddWallerTotal:
				return responseJSON_1('---------------对账成功------------------！')
			else:
				return responseJSON_0('---------------对账失败！---------------')
		else:
			return responseJSON_0('对账数据异常', '对账ID:{}'.format(time))
	else:
		return responseJSON_0('初始化数据异常', '初始化ID:{}'.format(time))


if __name__ == '__main__':
	print_warn_(checking(1605062253))
