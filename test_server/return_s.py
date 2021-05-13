import sys
def returnType(code=1,msg='',data=''):
	returnData = {
		'code':code,
		'mag':msg,
		'table_s':data
	}
	# return (sys._getframe().f_code.co_name)
	return returnData

