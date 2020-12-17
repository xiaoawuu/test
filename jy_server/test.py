import random
from test_server.data import mysqls
print()

def addData(ren):
	i = 1
	while i < ren:
		mobile = '1'+ str(random.randint(3000000000,9999999999))
		i = i+1
		re = mysqls.Data().query('localhost',"INSERT  INTO `data` (mobile) VALUES ('{}')".format(mobile))

addData(151)










