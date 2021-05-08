def responseJSON_1(msg='', data='', ):
	return {'code': 1, 'msg': msg, 'data': data}


def responseJSON_0(msg='', data='', ):
	return {'code': 0, 'msg': msg, 'data': data}


def responseJSON(msg='', data='', code=0):
	return {'code': code, 'msg': msg, 'data': data}
