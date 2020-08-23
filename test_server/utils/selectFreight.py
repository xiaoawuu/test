from test_server.data import mysqls


def selectFreight(orderList):
	list = []

	for i in orderList:
		print('循环：',i)
		sql = "SELECT freight_id FROM tms_wl_freight WHERE first_order_id ='{}';".format(i)
		data = mysqls.Data().query('tms_test', sql)
		list.append(data[0]['freight_id'])
	return list


# print(selectFreight(['LO-202008009378','LO-202008009377']))