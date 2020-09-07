import time


def writeLog(title, data):
	try:
		path = 'C:\\test_server\\test_server\\timedTask\log.log'
		time_ = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		with open(path, "a", encoding="utf-8") as f:
			f.write('[{}]>>>>>>执行时间:{}'.format(title, time_) + "\n" + '{}'.format(data) + '\n\n')
			return True
	except Exception as e:
		return '异常：{}'.format(e)
	finally:
		f.close()
