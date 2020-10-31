import selenium
import time
from appium import webdriver
from test_server.appium_android.utils.config import config as con
from test_server.appium_android.ElementModules.location_element import *
from test_server.appium_android.ElementModules.LoginAndRegister import *
from test_server.appium_android.utils.Assert import *
from test_server.appium_android.utils.getToast import getToast


class Case():
	def __init__(self):
		self.account = '18007530115'
		self.pwd = '000000'
		self.code = '9514'
		self.invite_code = 'AB53495F48B31C5B'
		self.con = con("miui", "jy")
		self.con['newCommandTimeout'] = '3000'
		self.con['automationName'] = 'True'
		self.con['noReset'] = 'True'
		self.con['automationName'] = 'uiautomator2'
		print(self.con)

		print('selenium version = ', selenium.__version__)
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.con)
		time.sleep(1)

	def addAccount(self):
		self.driver.find_element_by_id(home_mobile_enroll).click()
		time.sleep(1)
		self.driver.find_element_by_id(enroll_account_input).send_keys(self.account)
		self.driver.find_element_by_id(enroll_code_input).send_keys(self.code)
		self.driver.find_element_by_id(enroll_password_input).send_keys(self.pwd)
		self.driver.find_element_by_id(enroll_button).click()
		time.sleep(0.5)
		self.driver.find_element_by_id(gender_man).click()
		self.driver.find_element_by_id(gender_send).click()
		time.sleep(0.5)
		self.driver.find_element_by_id(gender_dialog_confirm).click()
		self.driver.find_element_by_id(invitation_code).send_keys(self.invite_code)
		time.sleep(0.5)
		self.driver.find_element_by_id(invitation_code_send).click()
		self.driver.implicitly_wait(5)
		self.driver.find_element_by_id(upload_photo).click()
		time.sleep(0.5)
		try:
			self.driver.find_element_by_id('android:id/button1').click()
		except:
			pass
		self.driver.tap([(400, 997), (1080, 2280)], 500)
		self.driver.find_element_by_id('com.fcx.jy:id/check').click()
		self.driver.tap([(1000, 2220), (1080, 2280)], 500)
		time.sleep(0.5)
		self.driver.find_element_by_id(tailor_affirm).click()
		time.sleep(0.5)
		self.driver.find_element_by_id(user_name_input).send_keys('憨憨大叔')
		self.driver.find_element_by_id('com.fcx.jy:id/tv_chengshi').click()
		time.sleep(0.5)
		self.driver.tap([(730, 330), (1080, 2280)], 500)

		self.driver.find_element_by_id('com.fcx.jy:id/queding_tv').click()

		self.driver.find_element_by_id(birthday).click()
		self.driver.find_element_by_id('com.fcx.jy:id/queding_tv').click()
		# 选择职业
		self.driver.find_element_by_id(profession).click()
		time.sleep(0.5)
		self.driver.tap([(730, 330), (1080, 2280)], 500)

		self.driver.find_element_by_id(program).click()

		self.driver.tap([(590, 890), (1080, 2280)], 500)

		self.driver.find_element_by_id(gender_dialog_confirm).click()
		# 期望对象
		self.driver.find_element_by_id(expect_object).click()

		self.driver.tap([(550, 880), (1080, 2280)], 500)
		time.sleep(0.5)
		self.driver.find_element_by_id(gender_dialog_confirm).click()
		# 填写微信
		self.driver.find_element_by_id(wechat).send_keys('weixinhao')
		self.driver.find_element_by_id('com.fcx.jy:id/hide_wechat_view').click()


		size = self.driver.get_window_size()
		width = size.get('width')
		heights = size.get('height')

		print(size)


		start_x_end = width * 0.5

		start_y = heights * 0.8

		end_y = heights * 0.2

		self.driver.swipe(start_x_end, start_y, start_x_end, end_y)

		# 身高
		self.driver.find_element_by_id(height).click()
		time.sleep(0.5)
		self.driver.tap([(540, 1450), (1080, 2280)], 500)

		# 体重
		self.driver.find_element_by_id(weight).click()
		time.sleep(0.5)
		self.driver.tap([(540, 1480), (1080, 2280)], 500)
		self.driver.find_element_by_id(introduction).send_keys('比较看感觉')
		self.driver.find_element_by_id(send_data).click()
		time.sleep(5)




	def Login(self):
		print("addAccount")
		self.driver.find_element_by_id(home_login_button).click()
		self.driver.find_element_by_id(login_account_input).send_keys("18007530111")
		self.driver.find_element_by_id(login_password_input).send_keys("0000000")
		self.driver.find_element_by_id(login_button).click()
		is_true = assertIn(getToast(self.driver,"账号或密码错误"),'聚缘公园：账号或密码错误')


c = Case()
c.addAccount()
print("exit!")
