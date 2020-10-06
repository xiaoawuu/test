
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



# from appium import webdriver
# # 设置appium的配置
# desired_caps = {}
# desired_caps['platformName'] = 'Android'    #手机类型
# desired_caps['platformVersion'] = '8.1.0'   #手机操作系统版本
# desired_caps['deviceName'] = 'b649c4d'   #使用的手机或模拟器类型
# desired_caps['appPackage'] = 'com.fcx.jy'   # 使用的apk包名
# desired_caps['appActivity'] = 'com.fcx.jy.ui.activity.LoginActivity'              # 应用包名
# driver = webdriver.Remote('http://127.0.0.1:5233/wd/hub', desired_caps)  #调用appium的驱动
# # 定位元素
# driver.find_element_by_name("9").click()
# driver.find_element_by_name("6").click()
# # 退出程序
# driver.quit()



















