
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
		"token": "11f5c702add3d09c8159ece4a81913d5",
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
