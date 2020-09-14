
mobile = {}
import requests, json


def requestsPort(user_id, new_mobile):
	'''
	TP5修改手机号
	:param user_id:
	:param new_mobile:
	:return:
	'''
	# url=None
	url = "https://myadmin-api.zyb56.com/customer/changeUserMobile"
	re_data = {
		"token": "c1c95d62b91af8d7bb8e03a38e6b5215",
		"id": str(user_id),
		"mobile": new_mobile
	}
	try:
		headers = {
			"Content-Type": "application/json; charset=UTF-8"
		}
		response = requests.post(url, data=json.dumps(re_data), headers=headers)
		return response.json()
	except:
		return '异常'


from test_server.data.mysqls import Data


def updateMobile():
	for index, i in mobile.items():
		print('index:', index, "i", i)
		user_id = Data().query('zyb_live_r',
							   "SELECT id FROM `zyb_db`.`zyb_customer` WHERE `mobile` = '{}';".format(index))
		if user_id == ():
			continue
		print('user_id：', user_id[0]["id"], '旧手机号：', index, '新手机号：', i)
		print(requestsPort(user_id[0]["id"], i))

# 执行前查询下手机号是否已存在
# updateMobile()























