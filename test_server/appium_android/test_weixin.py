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
		# self.driver.press_keycode(26)
		# time.sleep(1)
		# self.driver.press_keycode(3)
		time.sleep(1)

	def is_true(self):
		print(2)
		self.driver.find_element_by_id("com.tencent.mm:id/ef9").click()
		time.sleep(0.5)
		self.driver.tap([(810, 444), (1050, 2160)], 500)
		time.sleep(0.5)
		data = sql_select("SELECT TOP 200 id ,wechat FROM biz_user WHERE sex = 2 AND wechat != '' and	len(wechat) BETWEEN 6 and	20 AND is_valid != 0;")
		for i in data:
			wx = i[1]
			self.driver.find_element_by_id("com.tencent.mm:id/fcn").click()
			time.sleep(0.5)
			self.driver.find_element_by_id("com.tencent.mm:id/bhn").send_keys(wx)
			time.sleep(0.5)
			self.driver.find_element_by_id("com.tencent.mm:id/bhn").click()
			time.sleep(0.5)
			self.driver.press_keycode(66)
			time.sleep(0.5)
			try:
				text = self.driver.find_element_by_id("com.tencent.mm:id/g6f").text
				if text == '添加到通讯录':
					print('真实的',wx)
				self.driver.press_keycode(4)
				time.sleep(0.5)
				self.driver.press_keycode(4)
				time.sleep(0.5)

			except Exception as ERR:
				time.sleep(0.5)
				self.driver.find_element_by_id("com.tencent.mm:id/aay").click()
				time.sleep(1)



a = WeChatIDCheck()
a.is_true()

config = {
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

# def test():
# 	a = sql_select(
# 		"SELECT TOP 200 id ,wechat FROM biz_user WHERE sex = 2 AND wechat != '' and	len(wechat) BETWEEN 6 and	20 AND is_valid != 0;")
# 	for i in a:
# 		a = i[1]
























