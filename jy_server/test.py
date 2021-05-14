import base64
import random

import requests
from test_server.data import mysqls
import json

def	parameterization():
	test = 'Alex'
	dict_s = {
		'name':'test',
		'user_id':0
	}
	print(json.dumps(dict_s).replace('test','ahua'))
	print(dict_s)


def test(port):


	a = mysqls.Data().query('localhost',"SELECT `key`,`value` FROM variable WHERE `port` = '{}';".format(port))
	dict_s = {}
	for i in a:
		if i['value'][0] == '{':
			dict_s[i['key']] = json.loads(i['value'])
			print(json.loads(i['value']))
		else:
			dict_s[i['key']] = i['value']

	print(json.dumps(dict_s, sort_keys=True, indent=4))


def kwargs(**kwargs):
	print(kwargs)
	print(str(kwargs).replace('{','').replace("}","").replace(':',"=").replace(","," AND "))

def args(*args):
	print(str(args).replace('(','').replace(")",""))

import datetime
def sql_get_tms_db_data(sql):
	query = mysqls.Data().query
	re_data = query('tms_test',sql)
	dict_a = {}
	for i in re_data:
		for s in i.keys():
			if type(i[s]) == datetime.datetime:
				print(type(i[s]))
				i[s] = i[s].strftime("%Y-%m-%d %H:%M:%S")
			dict_a[s] = i[s]
			print(s,':',i[s])
	print(dict_a)



# sql_get_tms_db_data("SELECT * FROM `tms_test`.`tms_wl_user` WHERE `user_name` = 'WLG0001'")



def	 add(freight):
	sql = '''
			SELECT
			freight_id 'waybill_sn',
			driver_mobile 'mobile',
			driver_number 'license',
			date_format(loading_date,'%Y-%m-%d') 'start_time',
			loading_x_y 'origin',
			unload_x_y 'destination',
			CONCAT(loading_province,loading_city,loading_district,loading_address) 'loading',
			CONCAT(unload_province,unload_city,unload_district,unload_address) 'unload'
		FROM
			tms_wl_freight A
			JOIN tms_wl_order_particulars B ON A.first_order_id = B.first_order_id 
		WHERE
			freight_id = '{}';
	'''.format(freight)
	query = mysqls.Data().query
	re_data = query('tms_test', sql)[0]
	headers = {
		'Content-Type': 'application/json'
	}

	url = "http://tms-test.zyb56.cn/basics/addTestLocation1"
	response = requests.request("POST", url, headers=headers, data=json.dumps(re_data))
	print(response.text)


def for_order(order_list):
	for i in order_list:
		add(i)


def	test_wl(freight):
	try:
		return int(freight) * 2
	except Exception:
		return '请输入数字'

print(test_wl(1))

def	test_wl(freight):
	url = "http://wl.test.zyb56.cn/api/invoice/paymentRejected"

	payload={'wlToken': 'wl_token_1618387050913940',
	'remark': '测试',
	'freightId': '{}'.format(freight)}
	files=[]
	headers = {
	  'Cookie': 'SESSION=3728b281-0a5f-4e4a-9060-9b8937a76411'
	}

	response = requests.request("POST", url, headers=headers, data=payload, files=files)
	print('aa')
	print(response.text)



def	reSignFrameWork(c_id):
	'''
	重签框架协议
	:return:
	'''
	url = "https://managerservice.zyb56.com/api/contract/reSignFrameWork"

	payload = {'sysToken': 'sys_token_16184536592489',
			   'cId': '{}'.format(c_id)}
	files = []
	headers = {}
	response = requests.request("POST", url, headers=headers, data=payload, files=files)

	print(response.text)


def for_list(order_list):
	for i in order_list:
		reSignFrameWork(i)
