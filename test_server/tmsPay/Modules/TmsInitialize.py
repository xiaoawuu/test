from test_server.tmsPay.Modules.GetWlWallet import sql_


def insert(c_id, ws_wallet,wl_wallet,pay_order_count):
	try:
		sql = """
			INSERT INTO tms_initialize ( c_id, ws_wallet, wl_wallet, pay_order_count ) VALUES ( %s, %e, %e, %s );
			""" % (c_id, float(ws_wallet),float(wl_wallet),int(pay_order_count))
		data = sql_('localhost', sql)
		print('insert',data)
		return data
	except TypeError as err:
		return err

# print(insert(1,1,"1",1))

