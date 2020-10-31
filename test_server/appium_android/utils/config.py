import configparser


def config(device, package):
	conf = configparser.ConfigParser()
	conf.read(r'C:\test_server\test\test_server\appium_android\utils\config.ini')
	platformName = conf.get(str(device), 'platformName')
	platformVersion = conf.get(str(device), 'platformVersion')
	deviceName = conf.get(str(device), 'deviceName')
	appActivity = conf.get(str(package), 'appActivity')
	appPackage = conf.get(str(package), 'appPackage')
	return {
		"platformName": platformName,
		"platformVersion": platformVersion,
		"deviceName": deviceName,
		"appPackage": appPackage,
		"appActivity": appActivity
	}
