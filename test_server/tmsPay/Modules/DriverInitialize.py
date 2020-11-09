# from test_server.tmsPay.initialize import sql_
import time
from test_server.tmsPay.utils.responseJSON import responseJSON_0,responseJSON_1
from test_server.data.mysqls import Data

sql_ = Data().query
'''
CREATE TABLE `driver_initialize` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键自增id',
  `user_id` int NOT NULL COMMENT '用户id',
  `mobile` varchar(68) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '手机号',
  `balance` decimal(11,2) NOT NULL DEFAULT '0.00' COMMENT '可用',
  `freeze` decimal(11,2) NOT NULL DEFAULT '0.00' COMMENT '冻结',
  `out` decimal(11,2) NOT NULL DEFAULT '0.00' COMMENT '提现中',
  `sum_balance` decimal(11,2) NOT NULL COMMENT '总余额',
  `time` varchar(32) DEFAULT NULL COMMENT '时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

'''
from test_server.tmsPay.utils.print_ import *

def delete(mobile, ):
	try:
		sql = "DELETE FROM `driver_initialize` WHERE mobile={};".format(mobile)
		sql_('localhost', sql)
		print_suc('删除成功:{}'.format(mobile))
		return responseJSON_1('删除成功:', mobile)
	except TypeError as err:
		return responseJSON_0('删除失败', err, )


def setDriverInitialize(user_id, mobile, balance, freeze, out, sum_balance, execute_time):
	try:
		sql = """
			INSERT INTO driver_initialize (user_id,mobile,balance,freeze,`out`,sum_balance,time) VALUES (%d,%s,%e,%e,%e,%e,%s)
			""" % (user_id, mobile, float(balance), float(freeze), float(out), float(sum_balance), str(execute_time))
		data = sql_('localhost', sql)
		return data
	except TypeError as err:
		return err


def grtDriverAddWaller(mobile):
	sql = "SELECT sum_balance - (SELECT sum_balance FROM driver_initialize WHERE mobile = '{}' ORDER BY id DESC LIMIT 1,1" \
		  ") waller FROM driver_initialize WHERE mobile = '{}' ORDER BY id DESC LIMIT 0,1;".format(mobile, mobile)
	re = sql_('localhost', sql)
	return re[0]['waller']
