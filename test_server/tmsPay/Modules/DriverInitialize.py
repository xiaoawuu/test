# from test_server.tmsPay.initialize import sql_
from test_server.data.mysqls import Data
sql_ = Data().query


def getDriverInitialize():
	pass

def setDriverInitialize(user_id,mobile,balance,freeze,out,sum_balance):
	try:
		sql = """
			INSERT INTO driver_initialize (user_id,mobile,balance,freeze,`out`,sum_balance) VALUES (%d,%s,%e,%e,%e,%e)
			""" % (user_id, mobile, float(balance), float(freeze),float(out),float(sum_balance))
		data = sql_('localhost', sql)
		print('insert', data)
		return data
	except TypeError as err:
		return err
