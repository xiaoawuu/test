from test_server.data.mysqls import Data
sql_ = Data().query
def insert(c_id, ws_wallet,wl_wallet,pay_order_count,invoice_wallet):
	print('{}'.format(float(invoice_wallet)))
	try:
		sql = """
			INSERT INTO tms_initialize ( c_id, ws_wallet, wl_wallet, pay_order_count,invoice_wallet ) VALUES ( %s, %e, %e, %s ,%s);
			""" % (c_id, float(ws_wallet),float(wl_wallet),int(pay_order_count),str(invoice_wallet))
		print(sql)
		data = sql_('localhost', sql)
		return data
	except TypeError as err:
		return err
