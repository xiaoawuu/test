import selenium
import time
from appium import webdriver

# adevice = {
#     "platformName": "Android",
#     "platformVersion": "8.1.0",  # adb shell getprop ro.build.version.release
#     "deviceName": "b649c4d",  # adb devices
#     "appPackage": "com.fcx.jy",
#     'newCommandTimeout': "3000",
#     "automationName": "uiautomator2",
#     "appActivity": "com.fcx.jy.ui.activity.LoginActivity"
# }
from test_server.data.sql import sql_select

adevice = {
	"platformName": "Android",
	"platformVersion": "8.1.0",
	"deviceName": "b649c4d",
	"appPackage": "com.tencent.mm",
	'newCommandTimeout': "3000",
	"automationName": "uiautomator2",
	"appActivity": ".ui.LauncherUI",
	"dontStopAppOnReset": "True",
	"noReset": "True"
}
import os


# print('selenium version = ', selenium.__version__)
# driver = webdriver.Remote('http://localhost:4723/wd/hub', adevice)
#
# driver.find_element_by_id("com.tencent.mm:id/ef9").click()
#
# time.sleep(1)
#
# driver.find_element_by_xpath(
# 	"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
#
# # 256686
# time.sleep(2)
#
# driver.find_element_by_id("com.tencent.mm:id/fcn").click()
# time.sleep(2)
# driver.find_element_by_id("com.tencent.mm:id/bhn").send_keys('aaaaaaaaaaaaaaa')
# time.sleep(2)
# driver.find_element_by_id("com.tencent.mm:id/bhn").click()
# time.sleep(2)
# driver.press_keycode(66)
# time.sleep(2)
# try:
#
# 	a = driver.find_element_by_id("com.tencent.mm:id/g6f").text
# 	print(a)
# except Exception as ERR:
# 	print("不存在！")


# def WeChatIsTrue():
# 	adevice = {
# 		"platformName": "Android",
# 		"platformVersion": "8.1.0",
# 		"deviceName": "b649c4d",
# 		"appPackage": "com.tencent.mm",
# 		'newCommandTimeout': "3000",
# 		"automationName": "uiautomator2",
# 		"appActivity": ".ui.LauncherUI",
# 		"dontStopAppOnReset": "True",
# 		"noReset": "True"
# 	}
# 	import os
#
# 	print('selenium version = ', selenium.__version__)
# 	driver = webdriver.Remote('http://localhost:4723/wd/hub', adevice)
#
# 	driver.find_element_by_id("com.tencent.mm:id/ef9").click()
#
# 	time.sleep(1)
# 	driver.tap([(810, 444), (1050, 2160)], 500)
#
# 	driver.find_element_by_id("com.tencent.mm:id/fcn").click()
#
# 	driver.find_element_by_id("com.tencent.mm:id/bhn").send_keys('aaaaaaaaaaaaaaa')
#
# 	driver.find_element_by_id("com.tencent.mm:id/bhn").click()
#
# 	driver.press_keycode(66)
#
# 	try:
# 		a = driver.find_element_by_id("com.tencent.mm:id/g6f").text
# 		print(a)
# 	except Exception as ERR:
# 		print("不存在！")
def ride_file(text):
	with open(r'C:\test_s\test_server\appium_android\utils\is_true', "a") as file:  # ”w"代表着每次运行都覆盖内容
		file.write(text + "\n")


class WeChatIDCheck(object):
	def __init__(self):
		config = {
			"platformName": "Android",
			"platformVersion": "8.1.0",
			"deviceName": "6342f6a7",
			"appPackage": "com.tencent.mm",
			'newCommandTimeout': "3000",
			"automationName": "uiautomator2",
			"appActivity": ".ui.LauncherUI",
			"dontStopAppOnReset": "True",
			"noReset": "True"
		}
		print('selenium version = ', selenium.__version__)
		time.sleep(2)
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', config)

		time.sleep(1)

	def is_true(self):
		print(2)
		self.driver.find_element_by_id("com.tencent.mm:id/ef9").click()
		time.sleep(0.5)
		self.driver.tap([(810, 444), (1050, 2160)], 500)
		time.sleep(0.5)
		data = sql_select(
			"SELECT TOP 3 id ,wechat FROM biz_user WHERE sex = 2 AND wechat != '' and	len(wechat) BETWEEN 6 and	20 AND is_valid != 0;")
		for i in data:
			wx = i[1]
			self.driver.find_element_by_id("com.tencent.mm:id/fcn").click()
			time.sleep(0.3)
			self.driver.find_element_by_id("com.tencent.mm:id/bhn").send_keys(wx)
			time.sleep(0.3)
			self.driver.find_element_by_id("com.tencent.mm:id/bhn").click()
			time.sleep(0.3)
			self.driver.press_keycode(66)
			time.sleep(0.3)
			try:
				text = self.driver.find_element_by_id("com.tencent.mm:id/g6f").text
				if text == '添加到通讯录':
					ride_file('{}:{}'.format(i[0], wx))

					print('真实的', wx)
				self.driver.press_keycode(4)
				time.sleep(0.3)
				self.driver.press_keycode(4)
				time.sleep(0.3)

			except Exception as ERR:
				time.sleep(0.3)
				self.driver.find_element_by_id("com.tencent.mm:id/aay").click()


# a = WeChatIDCheck()
# a.is_true()
import werobot

robot = werobot.WeRoBot(token='123456')


@robot.handler
def hello(messages):
	return 'hello!'


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 8080
