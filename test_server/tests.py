# print(sys.path)
from test_server.data import mysqls

'''
['C:\\test_server\\test_server',
 'C:\\test_server',
  'C:\\test_server\\bin\\test_port\\venv\\Scripts\\python37.zip',
   'C:\\install_file\\python3\\DLLs', 'C:\\install_file\\python3\\lib',
    'C:\\install_file\\python3', 'C:\\test_server\\bin\\test_port\\venv', 
    'C:\\test_server\\bin\\test_port\\venv\\lib\\site-packages', 
    'C:\\test_server\\bin\\test_port\\venv\\lib\\site-packages\\setuptools-40.8.0-py3.7.egg',
     'C:\\test_server\\bin\\test_port\\venv\\lib\\site-packages\\pip-19.0.3-py3.7.egg']
'''
def test():
	list = ['LO-202008009374', 'LO-202008009375', 'LO-202008009376', 'LO-202008009377', 'LO-202008009378']
	dict = {}
	for i in list:
		print('循环：',i)
		sql = "SELECT freight_id FROM tms_wl_freight WHERE first_order_id ='{}';".format(i)
		data = mysqls.Data().query('tms_test', sql)
		dict[i] = data[0]['freight_id']
	return dict
# print(max('4','0','1'))

a= mysqls.Data().query('zyb_test',"SELECT id,bank,number FROM `zyb_pay_bankcard` WHERE bank_authid = '4414811099907211134' AND	del != 1 ORDER BY id DESC LIMIT 1;")
if len(a) != 0:
	print(a)
else:print(0)


