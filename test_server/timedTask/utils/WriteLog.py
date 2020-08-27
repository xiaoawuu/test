import time
def writeLog(title,data):
	try:
		path = 'C:\\test_server\\test_server\\timedTask\log.log'
		time_ = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		with open(path,"a", encoding="utf-8") as f:    #设置文件对象
			f.write('[{}]>>>>>>执行时间:{}'.format(title,time_) + "\n" + '{}'.format(data) + '\n\n')    #可以是随便对文件的操作
			return True
	except Exception as e:
		return '异常：{}'.format(e)
	finally:
		f.close()
