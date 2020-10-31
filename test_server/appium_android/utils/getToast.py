from test_server.appium_android.utils.Assert import assertIn,assertEqual

def	getToast(driver,text):
	# text模糊定位
	driver.implicitly_wait(3)
	return driver.find_element_by_xpath('//*[contains(@text, "%s")]' % text).text

