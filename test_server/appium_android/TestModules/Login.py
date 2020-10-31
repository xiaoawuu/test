# coding=utf-8

import selenium
import time
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from test_server.appium_android.ElementModules import LoginAndRegister


def login():
	config = {
		"platformName": "Android",
		"platformVersion": "8.1.0",
		"deviceName": "6342f6a7",
		"appPackage": "com.fcx.jy",
		'newCommandTimeout': "3000",
		"automationName": "uiautomator2",
		"appActivity": "com.fcx.jy.ui.activity.LoginActivity",
		"dontStopAppOnReset": "False",
		"noReset": "True"}
	print('selenium version = ', selenium.__version__)
	driver = webdriver.Remote('http://localhost:4723/wd/hub', config)
	time.sleep(1)
	driver.find_element_by_id('com.fcx.jy:id/tv_login').click()
	time.sleep(0.5)
	driver.find_element_by_id(LoginAndRegister.account_input).send_keys('18007530111')
	time.sleep(0.5)
	driver.find_element_by_id(LoginAndRegister.password_input).send_keys('0000000')
	time.sleep(0.5)
	driver.find_element_by_id(LoginAndRegister.button).click()
	time.sleep(2)
	# 用于生成xpath定位 相当于 "//*[@text='没有找到用户名或密码']"
	text = '聚缘公园：账号或密码错'
	# text模糊定位
	driver.implicitly_wait(5)
	element = driver.find_element_by_xpath('//*[contains(@text, "%s")]' % text)
	assert element.text == '聚缘公园：账号或密码错'
	print(111111)
	print("toast内容：%s" % element.text)

login()
