# coding=utf-8

def responseJSON_1(msg='', data='', ):
	return {'code': 1, 'msg': msg, 'data': data}


def responseJSON_0(msg='', data='', ):
	return {'code': 0, 'msg': msg, 'data': data}


def responseJSON(msg='', data='', code=0):
	return {'code': code, 'msg': msg, 'data': data}
if __name__ == '__main__':
	print(responseJSON_0(msg='dssssss'))